---
x_pro_version: "1.1"
artifact: agent-rules
generated_from: [catalog, 00-PROJECT-PROFILE.md]
project: "{{ PROJECT_NAME }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
---

<!-- ============================================================ -->
<!-- GENERATED FILE — DO NOT EDIT BY HAND.                        -->
<!-- Compiled from the catalog's Required/Recommended blocks.    -->
<!-- To change a rule: edit the catalog and regenerate.          -->
<!-- Thin variants: CLAUDE.md · .cursorrules ·                   -->
<!--   .github/copilot-instructions.md (same flattened content). -->
<!-- ============================================================ -->

# Agent Rules

You are the developer of this project. Build **within these rails**.
This file is self-sufficient: everything you need is inline.

## Context
- Global tier: **{{ TIER_GLOBAL }}** — {{ POSTURE }}
- Dimensions raised by override: {{ ELEVATED_DIMENSIONS }}

## Required (non-negotiable)
<!-- Flattened from every Status=Required block. Each rule carries Do/Don't inline. -->

### {{ RULE_ID }} — {{ RULE_TITLE }}
- Do: {{ RULE_DO }}
- Don't: {{ RULE_DONT }}
- Example: `{{ RULE_EXAMPLE }}`

## Guardrails (Recommended)
<!-- Status=Recommended blocks. Follow unless justified in an ADR. -->
- {{ RECOMMENDED_RULE }}

## Out of scope (do not implement)
<!-- Deferred/Discarded blocks. Prevents the agent from "improving" beyond the Tier. -->
- {{ OUT_OF_SCOPE }}

## Before marking done
Meet `DEFINITION-OF-DONE.md` (also generated). Record an ADR in `ADR/` for architecture decisions.

---
*X-PRO.ai · version 1.1.0*
