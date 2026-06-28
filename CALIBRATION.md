# X-PRO.ai Catalog Calibration

Calibration is a process locked by **fixtures** (golden tests): canonical scenarios with
expected tier and statuses, re-run on every catalog change. A gate tweak that breaks another
scenario is caught by the fixture, not in production.

Canonical scenarios in `calibration/fixtures/`:
- `t0-poc` — floor (throwaway PoC, no sensitive data).
- `t2-expense` — real case (expense approval, security T3).
- `t3-regulated` — ceiling (healthcare, patient data, 24x7, big-data).

## Edge scenarios run

### T0 floor — no adjustment
Global tier T0. Result: ~6 "must decide" Required practices (presentation, classification,
model, hosting, compute) + the secrets ratchet (`APP-09`); everything else Discarded.
**Validation:** heavy rigor does not leak into a PoC, and the security ratchet works even at
the floor. No correction.

### T3 regulated ceiling — finding
Global tier T3, all dimensions T3 (`regulated` and `life-safety` overrides).
**Gap:** practices with `tier_required: null` never become Required, even at T3.
`DATA-03` (partitioning) stayed Recommended on a big-data system — it should be Required.
The gate only considered the tier; the practice is driven by the answer (`volume = big_data`).

## Refinements

### Refinement 1 — `deferrable` field (origin: T2 example)
The `BUS-05` (`fast_mvp`) modulation downgraded too many Recommended items, including cheap
hygiene (modular monolith, structured logs, basic CI/CD). Those are not gold-plating.

**Fix:** a `deferrable: true|false` field per practice (default `false`). `fast_mvp` only
downgrades Recommended items with `deferrable: true`.

| Practice | deferrable | Why |
|---|---|---|
| APP-02, APP-10 | true | DDD and extensibility are deferrable rigor |
| DATA-03, DATA-05, DATA-08 | true | partitioning, OLAP, lineage — incremental rigor |
| INFRA-05, INFRA-08, INFRA-10 | true | auto-scaling, full IaC, formal FinOps |
| APP-03, APP-05, APP-06 | false | modular monolith, timeout/retry, logs — cheap hygiene |
| DATA-10, INFRA-03, INFRA-07, INFRA-09 | false | no DB coupling, multi-AZ, gateway, basic CI/CD |
| (security dimension) | false | already exempt from modulation |

### Refinement 2 — answer-conditional gate (origin: T3 regulated)
Some practices are driven by the **answer**, not the tier. The tier scales the *rigor*;
the answer decides whether the practice *applies*.

**Fix:** the gate accepts `required_if: "<condition on the answer>"`, evaluated before the
tier. If it matches, the practice is Required regardless of tier.

| Practice | required_if |
|---|---|
| DATA-03 | `volume in [high, big_data_streaming]` |
| DATA-05 | `access == mixed` (OLTP+OLAP coexist → separate) |
| INFRA-05 | `scaling in [auto_scaling, elastic_serverless]` |
| INFRA-08 | `provisioning in [iac_terraform_cdk, gitops]` |
| INFRA-09 | `deploy in [blue_green, canary]` |

> Interaction: if `required_if` matches, the practice is Required and never downgraded —
> `deferrable` only acts when the status resolved to Recommended.

## Patch: catalog 1.0.0 → 1.1.0
Minor with a caveat: it changes recommendations for `fast_mvp` projects (refinement 1) and for
projects whose answers trigger `required_if` (refinement 2). See `CHANGELOG.md`.
The updated gating function is in `GENERATOR-SPEC.md` (v1.1).

---
*X-PRO.ai · version 1.1.0*
