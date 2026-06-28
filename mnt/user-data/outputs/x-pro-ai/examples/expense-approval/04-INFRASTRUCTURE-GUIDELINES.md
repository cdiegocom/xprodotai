# Infrastructure — guidelines

<!-- GENERATED. Edit the catalog and regenerate. -->

### [INFRA-01] Hosting model — **Required**
- Do: Choose the model according to sovereignty, latency and operating capacity.
- Don't: Do not adopt multi-cloud without a real need — the complexity cost is high.
- Verification: The model meets DATA-07 residency and the BUS-08 operating model.

### [INFRA-02] Compute model — **Required**
- Do: Choose according to the load pattern and the BUS-08 operational maturity.
- Don't: Do not adopt Kubernetes without the operational capacity to sustain it.
- Verification: The model fits the load pattern and whoever operates it.

### [INFRA-03] Availability topology — **Recommended**
- Do: Size the topology to the SLO declared in NFR-01.
- Don't: Do not pay for multi-region for an SLO that doesn't require it.
- Verification: The topology sustains the NFR-01 SLO.

### [INFRA-04] RTO and recovery — **Required**
- Do: Define and rehearse the recovery plan proportional to the RTO.
- Don't: Do not declare an RTO without rehearsing recovery.
- Verification: The recovery rehearsal meets the NFR-02 RTO.

### [INFRA-05] Scalability — **Deferred**
- Do: Configure scaling according to the expected load variation.
- Don't: Do not over-provision fixed capacity for a rare peak — it's idle cost.
- Verification: The system absorbs the expected peak without violating NFR-05.
- Trade-off: Auto-scaling deferred. -> TRADE-OFFS.md

### [INFRA-06] Security posture — **Required**
- Do: Apply least privilege and segmentation per the DATA-01 classification.
- Don't: Do not expose internal resources without need.
- Verification: Access follows least privilege and segmentation by data class.

### [INFRA-07] Network and exposure — **Recommended**
- Do: Expose through the minimal necessary edge; add gateway/WAF and rate limit on public surfaces (T2+).
- Don't: Do not expose a database or internal service directly to the internet.
- Verification: Every public surface goes through a controlled edge.

### [INFRA-08] IaC and change management — **Deferred**
- Do: Version infrastructure as code from T2 onward.
- Don't: Do not change production manually without an audit trail.
- Verification: Infra changes are reproducible and auditable.
- Trade-off: Full IaC deferred. -> TRADE-OFFS.md

### [INFRA-09] CI/CD and deploy strategy — **Recommended**
- Do: Automate the pipeline and reduce release risk according to the tier.
- Don't: Do not depend on manual deploy at T2+.
- Verification: Deploy is automated and has a rollback path.

### [INFRA-10] Cost and sustainability — **Deferred**
- Do: Monitor cost per unit of value and right-size periodically.
- Don't: Do not leave idle resources without review.
- Verification: Cost visibility exists and optimization actions are active.


---
*X-PRO.ai · catalog v1.1.0 · generator v1.1.0*
