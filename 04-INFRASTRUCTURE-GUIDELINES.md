---
x_pro_version: "1.1"
artifact: infrastructure-guidelines
project: "{{ PROJECT_NAME }}"
project_id: "{{ PROJECT_ID }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
source: x-pro-catalog/catalog/infrastructure.yaml
---

<!-- GENERATED from the catalog. Do not edit by hand: edit the catalog and regenerate. -->

# Infrastructure Guidelines

> Follows the canonical layer structure (see `02-APPLICATION-GUIDELINES.md`), swapping the
> ID prefix to `INFRA` and the set of 10 questions. Infrastructure blocks mix Tier gates,
> `required_if` (answer-driven) and security `override` (ratchet — can only raise the Tier).

## How to read this file

Each guideline is a **decision block** rendered from a catalog record. Fixed schema:

```
### [INFRA-NN] Title
- Status:     Required | Recommended | Deferred | Discarded
- Gate:       tier_required=TX · tier_recommended=TY · dimension=<name> (effective TZ)
- Origin:     INFRA-QN = "<answer>"
- Reference:  <framework> · <pillar> · <practice>
- Directive:  Do / Don't / Example / Verification   (structured, varies by tier)
- Trade-off:  link to TRADE-OFFS.md if Deferred/Discarded
```

`Do`/`Don't` compile to `AI-AGENT-RULES.md` and `Verification` compiles to
`DEFINITION-OF-DONE.md`. One record, several destinations.

---

### [INFRA-06] Security posture
- **Status:** {{ INFRA06_STATUS }}
- **Gate:** tier_required=T1 · tier_recommended=T2 · override "regulated -> zero_trust/T3" · dimension=security (effective {{ TIER_SEC }})
- **Origin:** INFRA-Q6 = "{{ INFRA_Q6 }}"
- **Reference:** AWS WAF · Security · defense-in-depth
- **Directive:**
  - **Do:** {{ INFRA06_DO }}
  - **Don't:** {{ INFRA06_DONT }}
  - **Example:** `{{ INFRA06_EXAMPLE }}`
  - **Verification:** {{ INFRA06_VERIFICATION }}
- **Trade-off:** {{ INFRA06_TRADEOFF }}  <!-- TRADE-OFFS.md#INFRA-06 if below gate -->

### [INFRA-09] CI/CD and deploy strategy
- **Status:** {{ INFRA09_STATUS }}
- **Gate:** tier_recommended=T1 · required_if "deploy in [blue_green, canary]" · dimension=operational (effective {{ TIER_OPS }})
- **Origin:** INFRA-Q9 = "{{ INFRA_Q9 }}"
- **Reference:** DORA · delivery · progressive-deploy
- **Directive:**
  - **Do:** {{ INFRA09_DO }}
  - **Don't:** {{ INFRA09_DONT }}
  - **Verification:** {{ INFRA09_VERIFICATION }}
- **Trade-off:** {{ INFRA09_TRADEOFF }}  <!-- TRADE-OFFS.md#INFRA-09 if recommended-but-deferred -->

<!-- xpro: the remaining blocks (INFRA-01,02,03,04,05,07,08,10) follow the same schema. Generate in full. -->

## Additional context (user input)
{{ INFRA_CONTEXT_FREE_TEXT }}

---
*X-PRO.ai · version 1.1.0*
