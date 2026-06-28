# X-PRO.ai — Extreme Software Process for AI Driven-Development

A framework that produces a **library of instructions telling an AI coding agent how to build a
specific project** — with the engineering rigor *calibrated to that project's real criticality and
complexity*, instead of applying every best practice everywhere.

The output is a set of plain Markdown artifacts an agent (Claude Code, Cursor, Copilot, or any
generic LLM agent) reads as guardrails. The same global catalog of practices produces a
throwaway-PoC ruleset or a regulated-system ruleset depending on the answers — and **every choice
to include, defer, or drop a practice is recorded with its reason**.

> *X-PRO.ai · version 1.1.0*

---

## The problem it solves

Best-practice catalogs (AWS/Azure Well-Architected, Google SRE, 12-factor, DORA) describe what
*excellent* systems do. Applied literally to a two-week internal tool, they are wasteful; applied
loosely to a payment platform, they are dangerous. The hard part is not knowing the practices —
it's deciding **how much of each** a given project warrants, and being honest about what you chose
to skip.

X-PRO.ai treats that calibration as a first-class, auditable computation. You profile the project
once; a **Tier** is derived; the Tier modulates each practice from `Required` down to `Discarded`;
and the trade-offs are written down rather than left implicit.

It is a **trade-off engine, not a "best of all worlds" template.**

---

## Mental model

```
        answers                Tier (Layer 0)            gating               artifacts
   ┌──────────────┐        ┌──────────────────┐     ┌──────────────┐     ┌──────────────────┐
   │ criticality  │        │  Criticality (C) │     │  per-layer   │     │ 00-PROFILE       │
   │ complexity   │  ───►  │  Complexity  (K) │ ──► │  decision    │ ──► │ 01..04 layers    │ ──► AI agent
   │ 4 batteries  │        │  → base tier T0-3│     │  blocks      │     │ TRADE-OFFS / DoD │     reads
   │ flags        │        │  + overrides     │     │  Req/Rec/Def │     │ AI-AGENT-RULES   │     AI-AGENT-RULES.md
   └──────────────┘        └──────────────────┘     └──────────────┘     └──────────────────┘
```

One catalog (the *data*) + your answers → one calibrated instance (the *artifacts*). Change the
catalog and every project that upgrades inherits the improvement; change the answers and only that
project's artifacts move.

---

## How it works

### 1. Layer 0 — profiling produces a Tier

Two independent axes are scored from short questionnaires:

- **Criticality (C)** — 5 questions, each 0–3 (sum 0–15): impact of failure, data sensitivity,
  blast radius, expected SLA, reversibility.
- **Complexity (K)** — 4 questions, each 0–2 (sum 0–8): domain, integrations, data, distribution.

Each sum falls into a band:

| Criticality band | Range | | Complexity band | Range |
|---|---|---|---|---|
| C-Low | 0–3 | | K-Low | 0–3 |
| C-Med | 4–7 | | K-Med | 4–6 |
| C-High | 8–11 | | K-High | 7–8 |
| C-Critical | 12–15 | | | |

The band pair maps to a **base Tier** via a matrix:

| | K-Low | K-Med | K-High |
|---|---|---|---|
| **C-Critical** | T3 | T3 | T3 |
| **C-High** | T2 | T2 | T3 |
| **C-Med** | T1 | T2 | T2 |
| **C-Low** | T0 | T1 | T1 |

The Tiers read as: **T0** throwaway / PoC · **T1** internal, low-criticality · **T2** product ·
**T3** critical / regulated.

### 2. Overrides — a one-way ratchet

Some answers *floor* the Tier regardless of budget or deadline. Overrides only ever **raise** the
Tier, never lower it:

| Condition | Effect |
|---|---|
| Data is regulated | global floor **T3** |
| Data is PII / financial | `security` dimension floor **T2** |
| Payment / PCI flag | `security` dimension floor **T3** |
| Life-safety impact | global floor **T3** |

The result is a **global Tier plus a per-dimension Tier** for `reliability`, `security`,
`performance`, `cost`, `operational`, `sustainability`. A cost-conscious product can run at T2
globally while its `security` dimension is ratcheted to T3 by a payment flag.

### 3. Conflicts — detected, not blocked

When required rigor exceeds declared capacity (e.g. a 99.9% SLA against a "tight deadline / small
team" constraint), it is flagged as an **accepted risk** in `TRADE-OFFS.md`. Generation proceeds —
the point is a conscious decision, not a hard stop.

### 4. The four layers and the decision block

The project is described across the four Enterprise-Architecture layers, each a battery of 10
functional questions:

`01` **Business** · `02` **Application** · `03` **Data** · `04` **Infrastructure**

Every practice is a **decision block** rendered from one catalog record:

```
### [APP-05] Failure resilience
- Status:     Required | Recommended | Deferred | Discarded
- Gate:       tier_required=T3 · tier_recommended=T2 · dimension=reliability (effective T2)
- Origin:     APP-Q5 = "retries_timeouts"
- Reference:  AWS WAF · Reliability · resilience
- Directive:  Do / Don't / Example / Verification   (varies by tier)
- Trade-off:  link to TRADE-OFFS.md when Deferred/Discarded
```

### 5. Gating function — the answer decides *whether*, the Tier decides *how much*

```
teff = tier_by_dimension[ practice.dimension ]

# (1) does the practice apply at all?  — answer-driven
if   gate.required_if matches the answer        -> Required
elif gate.override   matches the answer         -> Required        # ratchet

# (2) how much rigor?  — tier-driven
elif teff >= gate.tier_required                 -> Required
elif teff >= gate.tier_recommended              -> Recommended
elif practice has a trade_off                   -> Deferred
else                                            -> Discarded

# (3) speed modulation — only relaxes deferrable, non-security rigor
if time_to_market == fast_mvp and status == Recommended
   and practice.deferrable and dimension != security:
    status = Deferred        # and recorded in TRADE-OFFS.md
```

`required_if` makes a practice mandatory because of *what the project is* (e.g. high data volume →
partitioning is Required no matter the Tier). The Tier then scales the rigor of everything else.
The `fast_mvp` modulation can soften *deferrable* recommendations — but never security, and never
anything already `Required`.

---

## Repository structure

Two packages with a deliberate separation of concerns.

```
.
├── README.md                         ← you are here (framework entry point)
│
├── x-pro-catalog/                    ← GLOBAL CATALOG  (the data + the engine; versioned on its own)
│   ├── catalog.yaml                  ← index, semver policy, contents map
│   ├── CHANGELOG.md                  ← what changed between catalog versions (read before upgrading)
│   ├── GENERATOR-SPEC.md             ← the 7-stage pipeline + gating function, as a spec
│   ├── catalog/
│   │   ├── tier-engine.yaml          ← Layer 0 as data: axes, bands, matrix, overrides, conflicts
│   │   ├── business.yaml             ← BUS-01..10
│   │   ├── application.yaml          ← APP-01..10
│   │   ├── data.yaml                 ← DATA-01..10
│   │   └── infrastructure.yaml       ← INFRA-01..10
│   ├── calibration/
│   │   ├── CALIBRATION.md            ← methodology + the edge cases that shaped v1.1
│   │   └── fixtures/                 ← golden tests: t0-poc, t2-expense, t3-regulated
│   └── tools/
│       ├── xpro_gen.py               ← the generator (implements GENERATOR-SPEC)
│       └── README.md                 ← generator usage
│
└── x-pro-ai/                         ← PROJECT SCAFFOLD  (templates + a worked instance)
    ├── README.md                     ← scaffold-specific guide
    ├── x-pro-manifest.yaml           ← machine-readable index of a project instance
    ├── x-pro.lock                    ← pins the catalog version (reproducibility)
    ├── 00-PROJECT-PROFILE.md         ← Layer-0 output template
    ├── 01-BUSINESS-CONSTRAINTS.md    ← layer templates (02 is the canonical structure;
    ├── 02-APPLICATION-GUIDELINES.md      01/03/04 mirror it with their own IDs/questions)
    ├── 03-DATA-GUIDELINES.md
    ├── 04-INFRASTRUCTURE-GUIDELINES.md
    ├── NFR.md                        ← non-functional targets (SLO, RTO/RPO, budgets)
    ├── SECURITY-BASELINE.md          ← minimum controls from classification + overrides
    ├── TRADE-OFFS.md                 ← what was Deferred/Discarded and why + reactivation triggers
    ├── DEFINITION-OF-DONE.md         ← gate checklist, per dimension and tier
    ├── AI-AGENT-RULES.md             ← imperative rules the agent reads to build within the rails
    ├── ADR/0000-template.md          ← Architecture Decision Record template
    └── examples/expense-approval/    ← a fully generated worked instance (see below)
```

**Why two packages.** The catalog is global and improves over time; projects *pin* a version via
`x-pro.lock` and upgrade deliberately. The scaffold holds the human-facing templates and one
worked example. The catalog is the single source of truth — no file should contradict
`00-PROJECT-PROFILE.md`.

---

## Getting started

### Prerequisites

- Python 3 and `pyyaml`:
  ```bash
  pip install pyyaml
  ```

### Run the regression suite

From inside the catalog package:

```bash
cd x-pro-catalog
python3 tools/xpro_gen.py test --catalog catalog --fixtures calibration/fixtures
```

This runs all golden fixtures and checks their asserts — the gate before bumping a catalog version.

### Generate a project's library

1. **Write an answers file** (`my-project.yaml`):

   ```yaml
   answers:
     criticality: { C1: 2, C2: 2, C3: 1, C4: 1, C5: 2 }   # → C sum, band
     complexity:  { K1: 1, K2: 1, K3: 1, K4: 1 }          # → K sum, band
     constraint:  { R1: 2 }                                # delivery pressure (drives fast_mvp)
     flags: [payment_pci]                                  # triggers specific overrides
     batteries:
       business:       { Q5: fast_mvp }
       application:    { Q5: retries_timeouts, Q7: oauth2_oidc }
       data:           { Q1: confidential }
       infrastructure: { Q5: fixed_manual }
   ```

2. **Generate:**

   ```bash
   cd x-pro-catalog
   python3 tools/xpro_gen.py generate \
       --catalog catalog \
       --answers my-project.yaml \
       --out ../path/to/your/project
   ```

3. **Commit the output** to your project repository.

4. **Point your AI agent at `AI-AGENT-RULES.md`** — it flattens the `Required`/`Recommended`
   directives into imperative rules the agent follows while building.

### What the generator emits

The generator renders these artifacts (plain filenames, each carrying an internal version footer):

`00-PROJECT-PROFILE.md` · `01-BUSINESS-CONSTRAINTS.md` · `02-APPLICATION-GUIDELINES.md` ·
`03-DATA-GUIDELINES.md` · `04-INFRASTRUCTURE-GUIDELINES.md` · `TRADE-OFFS.md` ·
`DEFINITION-OF-DONE.md` · `AI-AGENT-RULES.md`.

`NFR.md` and `SECURITY-BASELINE.md` ship as templates/skeletons in the scaffold; wiring them into
the generator's render step is a planned addition (they are listed as `pending` in the manifest).

---

## Worked example — `x-pro-ai/examples/expense-approval/`

An internal expense-approval platform: ~2,000 employees, integrates an ERP and a payment gateway,
built by a small team under a tight deadline.

- Scores: **C = 8 (C-High)**, **K = 4 (K-Med)** → base **T2**.
- `payment_pci` flag → `security` ratcheted to **T3**.
- Conflict flagged: required execution rigor (T2/T3) exceeds the declared team/deadline capacity →
  recorded as an accepted risk.
- Resulting status mix: **25 Required · 7 Recommended · 8 Deferred**. The 8 Deferred items each
  appear in `TRADE-OFFS.md` with a reactivation trigger.

The example is generated by the same generator from `calibration/fixtures/t2-expense.yaml`, so it
stays in lock-step with the catalog.

---

## Versioning model

- **Catalog** is versioned with **semver** (`catalog.yaml` → `version`). The policy: *major* changes
  an existing recommendation (upgrading alters artifacts); *minor* adds practices/questions
  (backward-compatible); *patch* is text/examples/references.
- **Generator** carries its own `GENERATOR_VERSION` (it implements a spec version independently of
  the catalog's data version).
- **`x-pro.lock`** pins the exact catalog version, an integrity hash, and an `answers_digest`. Same
  catalog version + same answers ⇒ byte-identical output (auditable, reproducible). If an answer
  changes, the digest diverges and the artifacts are flagged stale.
- **Filenames stay version-free** — Git tracks history and the files load cleanly into a Claude
  project. Instead, **every file declares its version internally**: a `# X-PRO.ai · version X.Y.Z`
  header comment in YAML/lock files, a `*X-PRO.ai · version X.Y.Z*` footer in Markdown, the
  generator's `GENERATOR_VERSION` constant, and a richer `catalog vX · generator vY` footer on
  generated artifacts.

---

## Extending the framework

- **Tune the Tier logic** by editing `catalog/tier-engine.yaml` — weights, bands, the matrix, and
  overrides are *data*, so changes are auditable diffs that never touch the generator.
- **Add or change a practice** by editing the relevant layer YAML (gates, directives,
  `verification`, `trade_off`, `deferrable`, `required_if`, references). The generator turns that
  data into every downstream artifact.
- **Guard against regressions** with fixtures: add a golden case under `calibration/fixtures/` and
  let `xpro_gen.py test` catch any gate tweak that breaks an edge scenario.
- **Logic vs. data:** gates, directives and trade-offs live in the catalog; the conditional logic
  (the gating function, override ratchet, conflict detection) lives in the generator. The catalog's
  prose conditions describe intent; the generator is the executable source of that logic.

---

## Reference frameworks

Practices trace back to: **AWS Well-Architected**, **Azure Well-Architected**, **Google SRE**,
**12-factor**, and **DORA** (with a few drawn from TOGAF, DAMA-DMBOK, and Fowler's evolutionary
design). Each decision block records its origin for traceability.

---

## Glossary

| Term | Meaning |
|---|---|
| **Tier (T0–T3)** | Calibrated rigor level; global and per-dimension |
| **Criticality / Complexity** | The two Layer-0 axes that derive the Tier |
| **Decision block** | One catalog record rendered into the artifacts |
| **Status** | `Required` · `Recommended` · `Deferred` · `Discarded` |
| **`required_if`** | Answer-driven mandate; fires regardless of Tier |
| **`override`** | Ratchet that floors a Tier (only ever raises) |
| **`deferrable`** | Whether `fast_mvp` may relax this recommendation |
| **`propagates`** | A constraint a (usually Business) decision imposes on other layers |
| **Trade-off** | A recorded `Deferred`/`Discarded` choice + its reactivation trigger |

---
*X-PRO.ai · version 1.1.0*
