---
x_pro_version: "1.1"
artifact: data-guidelines
project: "{{ PROJECT_NAME }}"
project_id: "{{ PROJECT_ID }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
source: x-pro-catalog/catalog/data.yaml
---

<!-- GENERATED from the catalog. Do not edit by hand: edit the catalog and regenerate. -->

# Data Guidelines

> Follows the canonical layer structure (see `02-APPLICATION-GUIDELINES.md`), swapping the
> ID prefix to `DATA` and the set of 10 questions. Several data blocks are gated by
> `required_if` — an **answer-driven** mandate that fires regardless of Tier when the
> profile answer matches.

## How to read this file

Each guideline is a **decision block** rendered from a catalog record. Fixed schema:

```
### [DATA-NN] Title
- Status:     Required | Recommended | Deferred | Discarded
- Gate:       tier_required=TX · tier_recommended=TY · dimension=<name> (effective TZ)
- Origin:     DATA-QN = "<answer>"
- Reference:  <framework> · <pillar> · <practice>
- Directive:  Do / Don't / Example / Verification   (structured, varies by tier)
- Trade-off:  link to TRADE-OFFS.md if Deferred/Discarded
```

`Do`/`Don't` compile to `AI-AGENT-RULES.md` and `Verification` compiles to
`DEFINITION-OF-DONE.md`. One record, several destinations.

---

### [DATA-01] Data classification
- **Status:** {{ DATA01_STATUS }}
- **Gate:** tier_required=T0 · tier_recommended=T0 · dimension=security (effective {{ TIER_SEC }})
- **Origin:** DATA-Q1 = "{{ DATA_Q1 }}"
- **Reference:** AWS WAF · Security · data-classification
- **Directive:**
  - **Do:** {{ DATA01_DO }}
  - **Don't:** {{ DATA01_DONT }}
  - **Verification:** {{ DATA01_VERIFICATION }}

### [DATA-03] Volume and growth
- **Status:** {{ DATA03_STATUS }}
- **Gate:** tier_recommended=T2 · required_if "volume in [high, big_data_streaming]" · dimension=performance (effective {{ TIER_PERF }})
- **Origin:** DATA-Q3 = "{{ DATA_Q3 }}"
- **Reference:** AWS WAF · Performance Efficiency · partitioning
- **Directive:**
  - **Do:** {{ DATA03_DO }}
  - **Don't:** {{ DATA03_DONT }}
  - **Example:** `{{ DATA03_EXAMPLE }}`
  - **Verification:** {{ DATA03_VERIFICATION }}
- **Trade-off:** {{ DATA03_TRADEOFF }}  <!-- TRADE-OFFS.md#DATA-03 if recommended-but-deferred (not required_if) -->

<!-- xpro: the remaining blocks (DATA-02,04,05,06,07,08,09,10) follow the same schema. Generate in full. -->

## Additional context (user input)
{{ DATA_CONTEXT_FREE_TEXT }}

---
*X-PRO.ai · version 1.1.0*
