# X-PRO.ai Generator Specification

The generator turns answers + a locked catalog into a library of artifacts.
It is **deterministic**: same answers + same catalog version = identical output, byte for byte.

## Inputs

- `answers.yaml` — Layer 0 answers + the 4 batteries + free-text context per layer.
- **Locked catalog** — resolved via `x-pro.lock` (`catalog.version` + `integrity`).
- **Metadata** — `project.name`, `stack`, `agent_target`.

## Pipeline (7 stages)

1. **Resolve and verify the catalog.** Read `x-pro.lock`, fetch the catalog at the pinned
   version and check the integrity hash. Mismatch → abort. This guarantees reproducibility
   even as the global catalog evolves.

2. **Compute the Tier (Layer 0).** Load `tier-engine.yaml`; sum the Criticality and
   Complexity scores; apply the bands; look up the matrix → `base tier`. Apply the overrides
   (ratchet: only raise) → `global tier` and the **per-dimension tiers**. Run conflict detection.

3. **Resolve each practice's status.** For each record in the 4 batteries: read the answer
   (`question_ref`), take the effective tier of the practice's `dimension` and apply the gating
   function (below) → `Required | Recommended | Deferred | Discarded`. Select the per-tier
   directive variant, resolving `inherits`.

4. **Propagate cross-layer constraints.** Process `propagates` and override effects
   (e.g. `DATA-01` forces encryption in `INFRA-06`/`SEC`). Apply the `BUS-05` (time-to-market)
   modulation and the `BUS-06` per-capability tiering.

5. **Record conflicts and trade-offs.** Stage-2 conflicts → "accepted risks" in `TRADE-OFFS.md`.
   Every `Deferred`/`Discarded` practice → an entry in `TRADE-OFFS.md` with the reactivation
   trigger from `trade_off`.

6. **Render the artifacts.** Apply the templates. Key points:
   - `DEFINITION-OF-DONE.md` is assembled from the `verification` fields, gated by tier.
   - `AI-AGENT-RULES.md` flattens the `Required`/`Recommended` items inline and produces the
     `agent_target` variant (`CLAUDE.md` / `.cursorrules` / `copilot-instructions.md`).
   - Stamp the `answers_digest` into the lock.

7. **Validate the output.** Coherence checks: nothing contradicts `00-PROJECT-PROFILE.md`;
   every `Required` has a DoD item; every `Deferred`/`Discarded` has a `TRADE-OFFS` entry;
   all cross-refs (`APP-04`↔`DATA-04`, `INFRA-04`↔`NFR-02`…) resolve.

## Gating function (core of stage 3) — v1.1

```
teff = tier_by_dimension[ practice.dimension ]

# 1. answer condition: does the practice apply? (calibration v1.1)
if gate.required_if matches the answer:                           -> Required
if gate.override matches the answer:                              -> Required   # ratchet

# 2. tier gating: how much rigor?
elif gate.tier_required != null and teff >= tier_required:        -> Required
elif gate.tier_recommended != null and teff >= tier_recommended:  -> Recommended
elif practice.trade_off exists:                                   -> Deferred
else:                                                             -> Discarded

# 3. BUS-05 modulation — only downgrades deferrable rigor (calibration v1.1)
if time_to_market == fast_mvp and status == Recommended
   and practice.deferrable == true and dimension != security:
    status = Deferred            # recorded in TRADE-OFFS
```

The answer decides whether the practice *applies* (`required_if`); the tier scales the *rigor*.

## From catalog field to artifact

| Catalog field | Feeds |
|---|---|
| `gate` + resolved status | layer `.md` block, `AI-AGENT-RULES.md` |
| `directive.do` / `dont` / `example` | `AI-AGENT-RULES.md` (Req./Rec.), layer `.md` |
| `directive.verification` | `DEFINITION-OF-DONE.md` (tier-gated) |
| `trade_off` | `TRADE-OFFS.md` |
| `propagates` / `override` | cross-layer effects, `SECURITY-BASELINE.md`, `NFR.md` |
| `reference` | traceability (WAF/SRE) in the layer `.md` |
| `tier-engine.yaml` + answers | `00-PROJECT-PROFILE.md` |

## Determinism and drift detection

The lock records `answers_digest` (a hash of the answers). If an answer changes the digest
diverges: the artifacts are stale and must be regenerated. Same catalog version + same answers
reproduce the library identically — a prerequisite for auditing and versioning the output.

## Error contract

- Catalog hash mismatch → abort (do not generate against a divergent version).
- Missing answer for a `question_ref` → abort, naming the question.
- A stage-2 conflict does **not** abort — it becomes an "accepted risk" and proceeds, requiring a conscious decision.
- Stage-7 validation failure → abort with the cross-ref that didn't resolve.

---
*X-PRO.ai · version 1.1.0*
