---
x_pro_version: "1.1"
artifact: adr
id: "ADR-{{ NNNN }}"
project_id: "{{ PROJECT_ID }}"
date: "{{ DATE }}"
status: "{{ STATUS }}"   # Proposed | Accepted | Superseded | Deprecated
---

# ADR-{{ NNNN }} — {{ TITLE }}

## Status
{{ STATUS }}  <!-- if Superseded, link the ADR that replaces it -->

## Context
{{ CONTEXT }}
<!-- xpro: what motivated the decision. Cite the Tier and source question where applicable. -->

## Decision
{{ DECISION }}
<!-- xpro: what was decided, in active voice. "We will use X because..." -->

## Alternatives considered
- {{ ALTERNATIVE }} — {{ WHY_NOT }}

## Consequences
- Positive: {{ POSITIVE }}
- Negative / costs: {{ NEGATIVE }}

## Links
- Profile: `../00-PROJECT-PROFILE.md`
- Related trade-off: `../TRADE-OFFS.md#{{ ANCHOR }}`
- Decision block: `{{ DECISION_BLOCK_ID }}`

---
*X-PRO.ai · version 1.1.0*
