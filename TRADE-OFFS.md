---
x_pro_version: "1.1"
artifact: trade-offs
project: "{{ PROJECT_NAME }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
---

# Trade-offs

Record of every `Deferred` or `Discarded` practice and why. This is the file that justifies
absences: when someone asks "why isn't X here?", the answer is here.

## Deferred
Practices that add value but not at the current Tier. Each has a review trigger.

| ID | Practice | Reason | Reactivate when |
|---|---|---|---|
| {{ TO_ID }} | {{ TO_PRACTICE }} | {{ TO_REASON }} | {{ TO_TRIGGER }} |

## Discarded
Practices deliberately out of scope for this project.

| ID | Practice | Reason |
|---|---|---|
| {{ TO_ID }} | {{ TO_PRACTICE }} | {{ TO_REASON }} |

## Accepted risks
Layer-0 conflicts the team consciously accepted.

| ID | Risk | Decision | Owner |
|---|---|---|---|
| {{ RISK_ID }} | {{ RISK }} | {{ DECISION }} | {{ OWNER }} |

---
*X-PRO.ai · version 1.1.0*
