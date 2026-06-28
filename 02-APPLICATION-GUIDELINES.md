---
x_pro_version: "1.1"
artifact: application-guidelines
project: "{{ PROJECT_NAME }}"
project_id: "{{ PROJECT_ID }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
source: x-pro-catalog/catalog/application.yaml
---

<!-- GENERATED from the catalog. Do not edit by hand: edit the catalog and regenerate. -->

# Application Guidelines

> **Canonical layer template.** `01-BUSINESS`, `03-DATA` and `04-INFRASTRUCTURE` follow this
> structure, swapping the ID prefix (`BUS`/`DATA`/`INFRA`) and the set of 10 questions.

## How to read this file

Each guideline is a **decision block** rendered from a catalog record. Fixed schema:

```
### [APP-NN] Title
- Status:     Required | Recommended | Deferred | Discarded
- Gate:       tier_required=TX · tier_recommended=TY · dimension=<name> (effective TZ)
- Origin:     APP-QN = "<answer>"
- Reference:  <framework> · <pillar> · <practice>
- Directive:  Do / Don't / Example / Verification   (structured, varies by tier)
- Trade-off:  link to TRADE-OFFS.md if Deferred/Discarded
```

`Do`/`Don't` compile to `AI-AGENT-RULES.md` and `Verification` compiles to
`DEFINITION-OF-DONE.md`. One record, several destinations.

---

### [APP-05] Failure resilience
- **Status:** {{ APP05_STATUS }}
- **Gate:** tier_required=T3 · tier_recommended=T2 · dimension=reliability (effective {{ TIER_REL }})
- **Origin:** APP-Q5 = "{{ APP_Q5 }}"
- **Reference:** AWS WAF · Reliability · resilience
- **Directive:**
  - **Do:** {{ APP05_DO }}
  - **Don't:** {{ APP05_DONT }}
  - **Example:** `{{ APP05_EXAMPLE }}`
  - **Verification:** {{ APP05_VERIFICATION }}
- **Trade-off:** {{ APP05_TRADEOFF }}  <!-- TRADE-OFFS.md#APP-05 if below gate -->

### [APP-07] AuthN / AuthZ
- **Status:** {{ APP07_STATUS }}
- **Gate:** tier_required=T1 · override "PII/regulated -> Required" · dimension=security (effective {{ TIER_SEC }})
- **Origin:** APP-Q7 = "{{ APP_Q7 }}"
- **Reference:** AWS WAF · Security · identity-access
- **Directive:**
  - **Do:** {{ APP07_DO }}
  - **Don't:** {{ APP07_DONT }}
  - **Verification:** {{ APP07_VERIFICATION }}

<!-- xpro: the remaining blocks (APP-01,02,03,04,06,08,09,10) follow the same schema. Generate in full. -->

## Additional context (user input)
{{ APP_CONTEXT_FREE_TEXT }}

---
*X-PRO.ai · version 1.1.0*
