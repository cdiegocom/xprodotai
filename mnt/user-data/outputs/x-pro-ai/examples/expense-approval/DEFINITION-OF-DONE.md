# Definition of Done — Tier T2

- [ ] The primary metric is measurable in production. `(BUS-01/Required)`
- [ ] Architecture decisions have a traceable ADR. `(BUS-02/Required)`
- [ ] Each obligation has a matching control in SECURITY-BASELINE. `(BUS-03/Required)`
- [ ] A budget and cost visibility exist (basic FinOps). `(BUS-04/Required)`
- [ ] Speed-driven deferrals are recorded with a review trigger. `(BUS-05/Required)`
- [ ] Critical modules have an effective tier equal to or higher than ancillary ones. `(BUS-06/Required)`
- [ ] Swapping a vendor does not require rewriting the domain. `(BUS-07/Required)`
- [ ] Critical flows have runbooks and operational toil is mapped. `(BUS-08/Required)`
- [ ] A retention/disposal policy consistent with the data's role exists. `(BUS-09/Required)`
- [ ] The level of extensibility is consistent with the declared horizon. `(BUS-10/Required)`
- [ ] The presentation layer contains no business logic. `(APP-01/Required)`
- [ ] Module boundaries are explicit; external integrations have an ACL. `(APP-03/Recommended)`
- [ ] Multi-step operations have a guarantee (transaction or saga). `(APP-04/Required)`
- [ ] Every external call has a timeout and retry policy. `(APP-05/Recommended)`
- [ ] Key metrics have a dashboard. `(APP-06/Recommended)`
- [ ] Access is authenticated and authorized; tenants isolated. `(APP-07/Required)`
- [ ] Integration covers the main flows. `(APP-08/Required)`
- [ ] No secret in code; configuration externalized. `(APP-09/Required)`
- [ ] Every dataset has an assigned classification. `(DATA-01/Required)`
- [ ] The chosen store fits the model and the DATA-05 access patterns. `(DATA-02/Required)`
- [ ] Critical invariants are guaranteed by the store or by saga. `(DATA-04/Required)`
- [ ] An expiration/disposal routine by policy exists. `(DATA-06/Required)`
- [ ] PII transits and rests only where permitted. `(DATA-07/Required)`
- [ ] Tested restore meets the RPO declared in NFR-03. `(DATA-09/Required)`
- [ ] Integrations do not depend on direct access to another schema. `(DATA-10/Recommended)`
- [ ] The model meets DATA-07 residency and the BUS-08 operating model. `(INFRA-01/Required)`
- [ ] The model fits the load pattern and whoever operates it. `(INFRA-02/Required)`
- [ ] The topology sustains the NFR-01 SLO. `(INFRA-03/Recommended)`
- [ ] The recovery rehearsal meets the NFR-02 RTO. `(INFRA-04/Required)`
- [ ] Access follows least privilege and segmentation by data class. `(INFRA-06/Required)`
- [ ] Every public surface goes through a controlled edge. `(INFRA-07/Recommended)`
- [ ] Deploy is automated and has a rollback path. `(INFRA-09/Recommended)`

---
*X-PRO.ai · catalog v1.1.0 · generator v1.1.0*
