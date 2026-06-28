---
x_pro_version: "1.1"
artifact: nfr
project: "{{ PROJECT_NAME }}"
generated: "{{ DATE }}"
tier_global: "{{ TIER_GLOBAL }}"
profile_ref: ./00-PROJECT-PROFILE.md
---

# Non-Functional Requirements (NFR)

Targets calibrated to the Tier. Every value below is a verifiable target, not an aspiration.
When the Tier does not require a target, the field reads `n/a (Tier {{ TIER_GLOBAL }})`.

## Availability and reliability
| ID | Target | Value | Tier origin |
|---|---|---|---|
| NFR-01 | Availability SLO | `{{ SLO_AVAIL }}` | reliability={{ TIER_REL }} |
| NFR-02 | RTO | `{{ RTO }}` | reliability={{ TIER_REL }} |
| NFR-03 | RPO | `{{ RPO }}` | reliability={{ TIER_REL }} |
| NFR-04 | Error budget | `{{ ERROR_BUDGET }}` | reliability={{ TIER_REL }} |

## Performance
| ID | Target | Value | Tier origin |
|---|---|---|---|
| NFR-05 | Latency p95 | `{{ LAT_P95 }}` | performance={{ TIER_PERF }} |
| NFR-06 | Throughput | `{{ THROUGHPUT }}` | performance={{ TIER_PERF }} |

## Security and data
| ID | Target | Value | Tier origin |
|---|---|---|---|
| NFR-07 | Data classification | `{{ DATA_CLASS }}` | security={{ TIER_SEC }} |
| NFR-08 | Encryption (rest/transit) | `{{ ENCRYPTION }}` | security={{ TIER_SEC }} |
| NFR-09 | Retention / disposal | `{{ RETENTION }}` | security={{ TIER_SEC }} |

## Cost and sustainability
| ID | Target | Value | Tier origin |
|---|---|---|---|
| NFR-10 | Budget / FinOps | `{{ COST_TARGET }}` | cost={{ TIER_COST }} |

<!-- xpro: tier gating reference when filling values
SLO:    T0 n/a · T1 ~99% · T2 99.9% · T3 99.95%+
RTO:    T0 best-effort · T1 hours · T2 < 1h · T3 minutes
RPO:    T0 n/a · T1 1 day · T2 < 1h · T3 ~0 (synchronous)
Tracing/error budget: introduce from T2. -->

---
*X-PRO.ai · version 1.1.0*
