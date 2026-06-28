---
x_pro_version: "1.1"
artifact: definition-of-done
project: "{{ PROJECT_NAME }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
---

# Definition of Done

Done gate. The agent does **not** mark a deliverable complete without meeting every `Required`
item of the current Tier. Each item shows the minimum Tier at which it becomes required.

## Application
- [ ] {{ DOD_APP_ITEM }}  `(min: T1)`
- [ ] {{ DOD_APP_ITEM }}  `(min: T2)`

## Tests
- [ ] {{ DOD_TEST_ITEM }}  `(min: T1)`
- [ ] {{ DOD_TEST_ITEM }}  `(min: T2)`
- [ ] {{ DOD_TEST_ITEM }}  `(min: T3)`

## Security
- [ ] {{ DOD_SEC_ITEM }}  `(min: {{ TIER_SEC }})`

## Observability
- [ ] {{ DOD_OBS_ITEM }}  `(min: T1)`
- [ ] {{ DOD_OBS_ITEM }}  `(min: T2)`

## Documentation
- [ ] README updated and ADRs recorded for relevant decisions  `(min: T1)`
- [ ] `TRADE-OFFS.md` reflects what was left out  `(min: T1)`

---
*X-PRO.ai · version 1.1.0*
