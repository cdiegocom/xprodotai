---
x_pro_version: "1.1"
artifact: business-constraints
project: "{{ PROJECT_NAME }}"
project_id: "{{ PROJECT_ID }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
source: x-pro-catalog/catalog/business.yaml
---

<!-- GENERATED from the catalog. Do not edit by hand: edit the catalog and regenerate. -->

# Business Constraints

> Follows the canonical layer structure (see `02-APPLICATION-GUIDELINES.md`), swapping the
> ID prefix to `BUS` and the set of 10 questions. Business decisions mostly do **not** become
> code — they become constraints and targets the other layers inherit, carried in a
> `Propagates` line.

## How to read this file

Each guideline is a **decision block** rendered from a catalog record. Fixed schema:

```
### [BUS-NN] Title
- Status:     Required | Recommended | Deferred | Discarded
- Gate:       tier_required=TX · tier_recommended=TY · dimension=<name> (effective TZ)
- Origin:     BUS-QN = "<answer>"
- Reference:  <framework> · <pillar> · <practice>
- Directive:  Do / Don't / Example / Verification   (structured, varies by tier)
- Propagates: constraint(s) inherited by APP / DATA / INFRA
- Trade-off:  link to TRADE-OFFS.md if Deferred/Discarded
```

`Do`/`Don't` compile to `AI-AGENT-RULES.md` and `Verification` compiles to
`DEFINITION-OF-DONE.md`. `Propagates` becomes an input constraint to the downstream layers.

---

### [BUS-01] Success metric (North Star)
- **Status:** {{ BUS01_STATUS }}
- **Gate:** tier_required=T1 · tier_recommended=T0 · dimension=operational (effective {{ TIER_OPS }})
- **Origin:** BUS-Q1 = "{{ BUS_Q1 }}"
- **Reference:** DORA · outcomes · north-star-metric
- **Directive:**
  - **Do:** {{ BUS01_DO }}
  - **Don't:** {{ BUS01_DONT }}
  - **Verification:** {{ BUS01_VERIFICATION }}
- **Propagates:** {{ BUS01_PROPAGATES }}  <!-- e.g. "Defines the focus of observability (APP-06)." -->

### [BUS-03] Compliance obligations
- **Status:** {{ BUS03_STATUS }}
- **Gate:** tier_required=T1 · tier_recommended=T1 · dimension=security (effective {{ TIER_SEC }})
- **Origin:** BUS-Q3 = "{{ BUS_Q3 }}"
- **Reference:** AWS WAF · Security · compliance
- **Directive:**
  - **Do:** {{ BUS03_DO }}
  - **Don't:** {{ BUS03_DONT }}
  - **Verification:** {{ BUS03_VERIFICATION }}
- **Propagates:** {{ BUS03_PROPAGATES }}  <!-- e.g. "Floors DATA-07 privacy and INFRA-06 posture." -->
- **Trade-off:** {{ BUS03_TRADEOFF }}  <!-- TRADE-OFFS.md#BUS-03 if below gate -->

<!-- xpro: the remaining blocks (BUS-02,04,05,06,07,08,09,10) follow the same schema. Generate in full. -->

## Additional context (user input)
{{ BUS_CONTEXT_FREE_TEXT }}

---
*X-PRO.ai · version 1.1.0*
