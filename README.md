# xpro_gen.py — X-PRO.ai Generator

Implements `GENERATOR-SPEC.md` (v1.1). Reads the catalog + answers, computes the Tier,
resolves each practice's status and renders the `.md` library. Runs the calibration fixtures
as a regression test.

## Usage

```bash
# Regression test (runs all fixtures and checks the asserts)
python3 tools/xpro_gen.py test --catalog catalog --fixtures calibration/fixtures

# Generate a project's library
python3 tools/xpro_gen.py generate \
    --catalog catalog \
    --answers calibration/fixtures/t2-expense.yaml \
    --out ./out
```

Requires `pyyaml` (`pip install pyyaml`).

## Answers input

A YAML with `answers:` (or the content directly):

```yaml
answers:
  criticality: { C1: 2, C2: 2, C3: 1, C4: 1, C5: 2 }
  complexity: { K1: 1, K2: 1, K3: 1, K4: 1 }
  constraint: { R1: 2 }
  flags: [payment_pci]               # triggers specific overrides
  batteries:
    business: { Q5: fast_mvp }
    application: { Q5: retries_timeouts, Q7: oauth2_oidc }
    data: { Q1: confidential }
    infrastructure: { Q5: fixed_manual }
```

## Catalog (data) vs. code (logic)

- **Catalog (data):** gates, directives, `verification`, `trade_off`, `deferrable`,
  `required_if`, reference mappings. Editing the catalog changes the output.
- **Code (logic):** the v1.1 gating function, tier overrides and conflict detection. The
  catalog's prose conditions (`C2 == regulated`) describe intent; the executable implementation
  of that logic lives here. `required_if` and gate `override`s are evaluated against the
  practice's own answer.

## Output

`00-PROJECT-PROFILE.md`, the four layer files, `TRADE-OFFS.md`, `DEFINITION-OF-DONE.md`,
`AI-AGENT-RULES.md` — all named `<NAME>.v<VERSION>.md` with a version footer.

## Determinism

Same answers + same catalog version = same output. Use `test` as the regression gate before
bumping a catalog version: if a gate tweak breaks an edge scenario, the fixture catches it.

---
*X-PRO.ai · version 1.1.0*
