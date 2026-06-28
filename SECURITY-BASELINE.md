---
x_pro_version: "1.1"
artifact: security-baseline
project: "{{ PROJECT_NAME }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
tier_security: "{{ TIER_SEC }}"
profile_ref: ./00-PROJECT-PROFILE.md
---

# Security Baseline

Minimum controls derived from **data classification** + effective security tier.
Override-driven items are `Required` regardless of budget (the ratchet does not lower them).

Current classification: **{{ DATA_CLASS }}** · Security tier: **{{ TIER_SEC }}**

### [SEC-01] Secrets management
- **Status:** {{ SEC01_STATUS }}
- **Gate:** tier_required=T1 · dimension=security (effective {{ TIER_SEC }})
- **Directive:** {{ SEC01_DIRECTIVE }}
  <!-- e.g. "Secrets in a vault / environment variables; never in the repository." -->

### [SEC-02] Encryption at rest
- **Status:** {{ SEC02_STATUS }}
- **Gate:** override if PII/financial · else tier_required=T2
- **Directive:** {{ SEC02_DIRECTIVE }}

### [SEC-03] Access logging and audit
- **Status:** {{ SEC03_STATUS }}
- **Gate:** override if regulated · else tier_required=T2
- **Directive:** {{ SEC03_DIRECTIVE }}

<!-- xpro: additional blocks per classification and tier
[SEC-04] AuthN/AuthZ (mirrors APP-07)
[SEC-05] Edge protection (WAF, rate limit) — from T2
[SEC-06] Vulnerability management / SCA in CI — from T2
[SEC-07] Data sovereignty / residency — if privacy-law/regulated -->

---
*X-PRO.ai · version 1.1.0*
