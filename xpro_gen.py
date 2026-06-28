#!/usr/bin/env python3
"""X-PRO.ai generator — implements GENERATOR-SPEC v1.1.

Reads the catalog + answers, computes the Tier (Layer 0), resolves each practice's
status via the v1.1 gating function and renders the .md library. Also runs the
calibration fixtures as a regression test.

Gates, directives and trade-offs come from the catalog (data). The conditional logic
(tier overrides, conflicts) is implemented here, since the catalog's prose conditions
describe intent; the code is the executable source of that logic.

Usage:
  xpro_gen.py generate --catalog DIR --answers FILE --out DIR
  xpro_gen.py test     --catalog DIR --fixtures DIR
"""
import sys, os, re, argparse, glob
import yaml

GENERATOR_VERSION = "1.1.0"   # tool version (implements GENERATOR-SPEC v1.1)

TIERS = ['T0', 'T1', 'T2', 'T3']
tmax = lambda a, b: a if TIERS.index(a) >= TIERS.index(b) else b
tge = lambda a, b: TIERS.index(a) >= TIERS.index(b)
LAYER = {'BUS': 'business', 'APP': 'application', 'DATA': 'data', 'INFRA': 'infrastructure'}
LAYER_FILE = {'business': '01-BUSINESS-CONSTRAINTS', 'application': '02-APPLICATION-GUIDELINES',
              'data': '03-DATA-GUIDELINES', 'infrastructure': '04-INFRASTRUCTURE-GUIDELINES'}
DIMS = ['reliability', 'security', 'performance', 'cost', 'operational', 'sustainability']
REQ, REC, DEF, DIS = 'Required', 'Recommended', 'Deferred', 'Discarded'


# ---------- loading ----------
def resolve_file(d, base, ext):
    """Find `base.ext` allowing an optional `.vX.Y.Z` version marker before the
    extension (e.g. business.v1.1.0.yaml). Prefers the highest versioned match;
    falls back to the unversioned name."""
    hits = sorted(glob.glob(os.path.join(d, f'{base}.v*.{ext}')))
    if hits:
        return hits[-1]
    plain = os.path.join(d, f'{base}.{ext}')
    if os.path.exists(plain):
        return plain
    raise FileNotFoundError(f'{base}.{ext} (versioned or plain) not found in {d}')


def load_catalog(path):
    cat = {'tier_engine': yaml.safe_load(open(resolve_file(path, 'tier-engine', 'yaml'))), 'layers': {}}
    for layer in LAYER.values():
        cat['layers'][layer] = yaml.safe_load(open(resolve_file(path, layer, 'yaml')))
    return cat


def load_answers(path):
    doc = yaml.safe_load(open(path))
    return doc['answers'] if 'answers' in doc else doc, doc


def read_version(catalog_dir):
    for d in (catalog_dir, os.path.dirname(os.path.abspath(catalog_dir))):
        try:
            cand = resolve_file(d, 'catalog', 'yaml')
        except FileNotFoundError:
            continue
        return (yaml.safe_load(open(cand)).get('catalog') or {}).get('version', '0.0.0')
    return '0.0.0'



# ---------- Layer 0 ----------
def band(value, bands):
    for name, (lo, hi) in bands.items():
        if lo <= value <= hi:
            return name


def is_sensitive(answers):
    return answers['criticality'].get('C2', 0) >= 2 or 'payment_pci' in answers.get('flags', [])


def is_mvp(answers):
    if answers.get('batteries', {}).get('business', {}).get('Q5') == 'fast_mvp':
        return True
    return answers.get('constraint', {}).get('R1', 0) >= 2


def compute_tier(answers, engine):
    crit, comp = answers['criticality'], answers['complexity']
    c_score, k_score = sum(crit.values()), sum(comp.values())
    c_band = band(c_score, engine['axes']['criticality']['bands'])
    k_band = band(k_score, engine['axes']['complexity']['bands'])
    base = engine['matrix'][c_band][k_band]
    tiers = {d: base for d in DIMS}
    g, applied = base, []
    C1, C2 = crit.get('C1', 0), crit.get('C2', 0)
    if C2 >= 3:
        g = tmax(g, 'T3'); applied.append('C2 regulated -> global T3')
    elif C2 == 2:
        tiers['security'] = tmax(tiers['security'], 'T2'); applied.append('financial/PII -> security T2')
    if 'payment_pci' in answers.get('flags', []):
        tiers['security'] = tmax(tiers['security'], 'T3'); applied.append('payment/PCI -> security T3')
    if C1 >= 3:
        g = tmax(g, 'T3'); applied.append('life-safety -> global T3')
    tiers = {d: tmax(t, g) for d, t in tiers.items()}
    conflicts = []
    if (tge(g, 'T2') or any(tge(tiers[d], 'T3') for d in DIMS)) and answers.get('constraint', {}).get('R1', 0) >= 2:
        conflicts.append('execution: required rigor (T2/T3) exceeds declared capacity (team/deadline)')
    return {'global': g, 'tiers': tiers, 'c_score': c_score, 'k_score': k_score,
            'c_band': c_band, 'k_band': k_band, 'base': base, 'overrides': applied, 'conflicts': conflicts}


# ---------- gating ----------
def practice_answer(pid, answers):
    prefix, num = pid.split('-')
    return answers.get('batteries', {}).get(LAYER[prefix], {}).get('Q%d' % int(num))


def eval_required_if(cond, answer):
    if answer is None:
        return False
    m = re.search(r'in\s*\[([^\]]*)\]', cond)
    if m:
        return answer in [o.strip() for o in m.group(1).split(',')]
    m = re.search(r'==\s*(\S+)', cond)
    return bool(m) and answer == m.group(1)


def override_fires(override, practice, answers, tiers):
    o = override.lower()
    if 'secret' in o:
        return True  # hard ratchet
    if 'public' in o:
        return practice_answer(practice['id'], answers) == 'simple_public' and is_sensitive(answers)
    if 'regulated' in o or 'pii' in o:
        return is_sensitive(answers)
    return False


def resolve_status(practice, answers, tier):
    dim = practice.get('dimension', 'operational')
    teff = tier['tiers'].get(dim, tier['global'])
    gate = practice.get('gate') or {}
    if gate.get('required_if') and eval_required_if(gate['required_if'], practice_answer(practice['id'], answers)):
        return REQ, teff
    if gate.get('override') and override_fires(gate['override'], practice, answers, tier['tiers']):
        return REQ, teff
    to, tr = gate.get('tier_required'), gate.get('tier_recommended')
    if to and tge(teff, to):
        status = REQ
    elif tr and tge(teff, tr):
        status = REC
    elif practice.get('trade_off'):
        status = DEF
    else:
        status = DIS
    if is_mvp(answers) and status == REC and practice.get('deferrable') is True and dim != 'security':
        status = DEF
    return status, teff


def resolve_all(catalog, answers, tier):
    res = {}
    for data in catalog['layers'].values():
        for p in data['practices']:
            status, teff = resolve_status(p, answers, tier)
            res[p['id']] = {'p': p, 'status': status, 'teff': teff,
                            'dim': p.get('dimension'), 'answer': practice_answer(p['id'], answers)}
    return res


# ---------- directive (resolve by tier + inherits) ----------
def resolve_inherits(d, t):
    block = dict(d.get(t, {}))
    parent = block.pop('inherits', None)
    if parent:
        base = resolve_inherits(d, parent)
        for k, v in block.items():
            if isinstance(v, list) and isinstance(base.get(k), list):
                base[k] = base[k] + v
            else:
                base[k] = v
        return base
    return block


def directive_for(practice, teff):
    d = practice.get('directive', {}) or {}
    if any(k in d for k in ('do', 'dont', 'example', 'verification')):
        return d
    chosen = None
    for t in TIERS:
        if t in d and tge(teff, t):
            chosen = t
    if chosen is None:
        chosen = next((t for t in TIERS if t in d), None)
    return resolve_inherits(d, chosen) if chosen else {}


# ---------- render ----------
def fmt_list(x):
    return '; '.join(x) if isinstance(x, list) else (x or '')


def render_profile(name, tier):
    L = [f'# Project Profile — {name}', '', '## Tier', '', '| Scope | Tier |', '|---|---|',
         f'| Global | `{tier["global"]}` |']
    for d in DIMS:
        L.append(f'| {d.capitalize()} | `{tier["tiers"][d]}` |')
    L += ['', '## Scores',
          f'- Criticality: {tier["c_score"]} ({tier["c_band"]}) · Complexity: {tier["k_score"]} ({tier["k_band"]}) -> base {tier["base"]}',
          '', '## Overrides'] + [f'- {o}' for o in tier['overrides'] or ['(none)']]
    L += ['', '## Conflicts'] + [f'- {c}' for c in tier['conflicts'] or ['(none)']]
    return '\n'.join(L) + '\n'


def render_layer(layer, data, res):
    L = [f'# {data["layer"].capitalize()} — guidelines', '', '<!-- GENERATED. Edit the catalog and regenerate. -->', '']
    for p in data['practices']:
        r = res[p['id']]
        d = directive_for(p, r['teff'])
        L.append(f'### [{p["id"]}] {p["title"]} — **{r["status"]}**')
        if d.get('do'):
            L.append(f'- Do: {fmt_list(d["do"])}')
        if d.get('dont'):
            L.append(f"- Don't: {fmt_list(d['dont'])}")
        if d.get('verification'):
            L.append(f'- Verification: {d["verification"]}')
        if r['status'] in (DEF, DIS) and p.get('trade_off'):
            L.append(f'- Trade-off: {p["trade_off"].get("record","")} -> TRADE-OFFS.md')
        L.append('')
    return '\n'.join(L) + '\n'


def render_agent_rules(name, tier, res):
    req, rec, out = [], [], []
    for pid, r in res.items():
        d = directive_for(r['p'], r['teff'])
        line = f'- {pid} {r["p"]["title"]}: {fmt_list(d.get("do"))}'
        if r['status'] == REQ:
            req.append(line)
        elif r['status'] == REC:
            rec.append(line)
        else:
            out.append(f'- {pid} {r["p"]["title"]} ({r["status"]}) — see TRADE-OFFS.md')
    L = ['<!-- GENERATED FILE — DO NOT EDIT BY HAND. -->', f'# Agent Rules — {name}',
         f'Global tier {tier["global"]}. Required items do not yield to deadlines.', '',
         '## Required (non-negotiable)'] + sorted(req)
    L += ['', '## Guardrails (Recommended)'] + sorted(rec)
    L += ['', '## Out of scope'] + sorted(out)
    return '\n'.join(L) + '\n'


def render_trade_offs(tier, res):
    L = ['# Trade-offs', '', '## Deferred / Discarded', '| ID | Status | Record | Reactivate when |', '|---|---|---|---|']
    for pid, r in res.items():
        if r['status'] in (DEF, DIS):
            t = r['p'].get('trade_off', {}) or {}
            L.append(f'| {pid} | {r["status"]} | {t.get("record","-")} | {t.get("reactivate_when","-")} |')
    L += ['', '## Accepted risks'] + [f'- {c}' for c in tier['conflicts'] or ['(none)']]
    return '\n'.join(L) + '\n'


def render_dod(tier, res):
    L = [f'# Definition of Done — Tier {tier["global"]}', '']
    for pid, r in res.items():
        if r['status'] in (REQ, REC):
            d = directive_for(r['p'], r['teff'])
            if d.get('verification'):
                L.append(f'- [ ] {d["verification"]} `({pid}/{r["status"]})`')
    return '\n'.join(L) + '\n'


def generate(catalog, answers, name, outdir, version):
    os.makedirs(outdir, exist_ok=True)
    tier = compute_tier(answers, catalog['tier_engine'])
    res = resolve_all(catalog, answers, tier)
    files = {'00-PROJECT-PROFILE.md': render_profile(name, tier),
             'AI-AGENT-RULES.md': render_agent_rules(name, tier, res),
             'TRADE-OFFS.md': render_trade_offs(tier, res),
             'DEFINITION-OF-DONE.md': render_dod(tier, res)}
    for layer, data in catalog['layers'].items():
        files[f'{LAYER_FILE[layer]}.md'] = render_layer(layer, data, res)
    footer = f'\n---\n*X-PRO.ai · catalog v{version} · generator v{GENERATOR_VERSION}*\n'
    written = {}
    for fn, content in files.items():
        # Filenames stay version-free (Git tracks history; stable names for the Claude project).
        # The version is identifiable INSIDE each file via the footer tag above.
        open(f'{outdir}/{fn}', 'w').write(content + footer)
        written[fn] = content
    return tier, res, written


# ---------- console output ----------
def print_summary(tier, res):
    print(f"Global tier: {tier['global']}  |  " + '  '.join(f'{d[:4]}={tier["tiers"][d]}' for d in DIMS))
    print(f"Scores: C={tier['c_score']}({tier['c_band']}) K={tier['k_score']}({tier['k_band']})")
    if tier['overrides']:
        print('Overrides: ' + '; '.join(tier['overrides']))
    if tier['conflicts']:
        print('Conflicts: ' + '; '.join(tier['conflicts']))
    counts = {}
    for r in res.values():
        counts[r['status']] = counts.get(r['status'], 0) + 1
    print('Status: ' + '  '.join(f'{k}={v}' for k, v in sorted(counts.items())))


# ---------- tests (fixtures) ----------
def check_assert(a, res):
    a = a.strip()
    m = re.match(r'^count\s+(\S+)\s*(==|>=|<=|>|<)\s*(\d+)$', a)
    if m:
        st, op, n = m.group(1), m.group(2), int(m.group(3))
        cnt = sum(1 for r in res.values() if r['status'] == st)
        ok = {'==': cnt == n, '>=': cnt >= n, '<=': cnt <= n, '>': cnt > n, '<': cnt < n}[op]
        return ok, f'count {st}={cnt}'
    m = re.match(r'^(\S+)\s*(==|!=)\s*(\S+)$', a)
    if m:
        pid, op, val = m.groups()
        actual = res.get(pid, {}).get('status')
        ok = (actual == val) if op == '==' else (actual != val)
        return ok, f'{pid}={actual}'
    return None, 'not checkable'


def run_fixture(catalog, path):
    fx = yaml.safe_load(open(path))
    answers = fx['answers']
    tier = compute_tier(answers, catalog['tier_engine'])
    res = resolve_all(catalog, answers, tier)
    exp = fx.get('expected', {})
    fails = []
    if 'tier_global' in exp and exp['tier_global'] != tier['global']:
        fails.append(f"tier_global expected {exp['tier_global']}, got {tier['global']}")
    for d, t in (exp.get('tiers') or {}).items():
        if tier['tiers'].get(d) != t:
            fails.append(f"tier[{d}] expected {t}, got {tier['tiers'].get(d)}")
    for a in exp.get('asserts', []):
        ok, detail = check_assert(a, res)
        if ok is False:
            fails.append(f"assert failed: {a} ({detail})")
    return fx.get('name', os.path.basename(path)), fails, tier, res


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    g = sub.add_parser('generate'); g.add_argument('--catalog', required=True)
    g.add_argument('--answers', required=True); g.add_argument('--out', required=True)
    g.add_argument('--name', default='Project'); g.add_argument('--version', default=None)
    t = sub.add_parser('test'); t.add_argument('--catalog', required=True); t.add_argument('--fixtures', required=True)
    args = ap.parse_args()
    catalog = load_catalog(args.catalog)

    if args.cmd == 'generate':
        answers, doc = load_answers(args.answers)
        name = doc.get('description', args.name)
        version = args.version or read_version(args.catalog)
        tier, res, files = generate(catalog, answers, name, args.out, version)
        print_summary(tier, res)
        print(f'Catalog v{version} · generator v{GENERATOR_VERSION} — generated {len(files)} files in {args.out}/')
    else:
        total_fail = 0
        for path in sorted(glob.glob(f'{args.fixtures}/*.yaml')):
            name, fails, tier, res = run_fixture(catalog, path)
            if fails:
                total_fail += 1
                print(f'X {name}: tier {tier["global"]}')
                for f in fails:
                    print(f'    - {f}')
            else:
                print(f'OK {name}: tier {tier["global"]} — all asserts passed')
        print('---')
        print('FAILED' if total_fail else 'ALL FIXTURES PASSED')
        sys.exit(1 if total_fail else 0)


if __name__ == '__main__':
    main()
