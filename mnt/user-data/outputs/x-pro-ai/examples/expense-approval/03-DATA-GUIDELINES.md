# Data — guidelines

<!-- GENERATED. Edit the catalog and regenerate. -->

### [DATA-01] Data classification — **Required**
- Do: Classify each dataset and propagate the tag to the store.
- Don't: Do not mix PII and public data in the same store without access control.
- Verification: Every dataset has an assigned classification.

### [DATA-02] Data model — **Required**
- Do: Choose the store according to the model and access patterns.
- Don't: Do not force relational onto data that is naturally graph or time-series.
- Verification: The chosen store fits the model and the DATA-05 access patterns.

### [DATA-03] Volume and growth — **Deferred**
- Do: Define indexes and partitioning proportional to the expected volume.
- Don't: Do not optimize for a scale that doesn't exist (at low volume).
- Verification: Hot queries have an acceptable plan at the expected volume.
- Trade-off: Aggressive sharding/partitioning deferred. -> TRADE-OFFS.md

### [DATA-04] Consistency and integrity — **Required**
- Do: Use ACID transactions where integrity is critical.
- Don't: Do not assume strong consistency in an eventually-consistent store.
- Verification: Critical invariants are guaranteed by the store or by saga.

### [DATA-05] Access patterns — **Deferred**
- Do: Separate OLTP from OLAP workloads when they coexist (read replica or CQRS).
- Don't: Do not run heavy analytics on the production transactional database.
- Verification: Analytical load does not degrade the transactional path.
- Trade-off: OLTP/OLAP separation deferred. -> TRADE-OFFS.md

### [DATA-06] Retention and disposal — **Required**
- Do: Define retention per class and automate disposal.
- Don't: Do not retain PII beyond what's necessary.
- Verification: An expiration/disposal routine by policy exists.

### [DATA-07] Privacy and sovereignty — **Required**
- Do: Anonymize or pseudonymize where applicable and respect data residency.
- Don't: Do not export PII to a non-permitted region.
- Verification: PII transits and rests only where permitted.

### [DATA-08] Lineage, quality and governance — **Deferred**
- Do: Record origin and validate quality at data ingestion.
- Don't: Do not trust external data without validation.
- Verification: Critical data has quality validation and traceable origin.
- Trade-off: Full lineage deferred. -> TRADE-OFFS.md

### [DATA-09] Backup and RPO — **Required**
- Do: Define backup according to the tier and test restore periodically.
- Don't: Do not assume the backup exists without testing restore.
- Verification: Tested restore meets the RPO declared in NFR-03.

### [DATA-10] Integration and movement — **Recommended**
- Do: Choose the mechanism according to latency and volume.
- Don't: Do not couple systems via direct access to another's database.
- Verification: Integrations do not depend on direct access to another schema.


---
*X-PRO.ai · catalog v1.1.0 · generator v1.1.0*
