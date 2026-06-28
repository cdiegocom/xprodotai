---
x_pro_version: "1.1"
artifact: project-profile
project: "{{ PROJECT_NAME }}"
project_id: "{{ PROJECT_ID }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
---

# Project Profile — Layer 0

> Source of truth for the Tier. The other artifacts derive from this file.

## Posture
{{ POSTURE }}
<!-- xpro: one sentence. e.g. "Internal product with a financial surface; elevated security, standard elsewhere." -->

## Tier

| Scope | Tier |
|---|---|
| Global | `{{ TIER_GLOBAL }}` |
| Reliability | `{{ TIER_REL }}` |
| Security | `{{ TIER_SEC }}` |
| Performance | `{{ TIER_PERF }}` |
| Cost | `{{ TIER_COST }}` |
| Operational | `{{ TIER_OPS }}` |
| Sustainability | `{{ TIER_SUST }}` |

`dimension_tier = max(global_tier, applicable_override)` — overrides only raise, never lower.

## Scores

| Axis | Score | Band |
|---|---|---|
| Criticality (0–15) | `{{ C_SCORE }}` | `{{ C_BAND }}` |
| Complexity (0–8) | `{{ K_SCORE }}` | `{{ K_BAND }}` |

Matrix cell: `{{ C_BAND }} × {{ K_BAND }}` → base Tier `{{ TIER_BASE }}`.

## Applied overrides
- {{ OVERRIDE }}  <!-- e.g. "Payment data (PCI) → security ≥ T3" -->

## Detected conflicts
- {{ CONFLICT }}  <!-- e.g. "Execution: required rigor (T2/T3) exceeds declared capacity (team/deadline)." -->

## Answers (appendix)

### Criticality
- C1 Impact of failure: `{{ C1 }}`
- C2 Data sensitivity: `{{ C2 }}`
- C3 Blast radius: `{{ C3 }}`
- C4 Expected SLA: `{{ C4 }}`
- C5 Reversibility: `{{ C5 }}`

### Complexity
- K1 Domain: `{{ K1 }}` · K2 Integrations: `{{ K2 }}` · K3 Data: `{{ K3 }}` · K4 Distribution: `{{ K4 }}`

### Execution constraint
- R1: `{{ R1 }}`

### Free-text context
{{ CONTEXT_FREE_TEXT }}

---
*X-PRO.ai · version 1.1.0*
