<!-- GENERATED FILE — DO NOT EDIT BY HAND. -->
# Agent Rules — Internal expense approval, ERP + payment gateway, small team / tight deadline.
Global tier T2. Required items do not yield to deadlines.

## Required (non-negotiable)
- APP-01 Presentation pattern: Adopt the pattern that fits the interaction: MVC (server-rendered), MVVM (SPA+API), hexagonal (headless), pipeline (batch/worker).
- APP-04 Consistency: Use transactions where integrity is critical; saga/outbox for consistency across services.
- APP-07 AuthN / AuthZ: Centralize identity (OIDC) and enforce authorization at the right point (gateway or service).; In multi-tenant, isolate data per tenant.
- APP-08 Testing strategy: Cover the critical path with unit tests.; Add integration tests and an agreed minimum coverage.
- APP-09 Configuration and secrets: Read config from environment variables; keep secrets in a vault.; Use feature flags to decouple deploy from release when useful.
- BUS-01 Success metric (North Star): Instrument the chosen metric explicitly from the MVP onward.
- BUS-02 Governance model: Record relevant decisions as ADRs.; Define who approves architecture changes.
- BUS-03 Compliance obligations: List the concrete obligations: minimum retention, residency, right to erasure.
- BUS-04 Revenue model and cost sensitivity: Set a cost ceiling and instrument spend per unit of value.
- BUS-05 Time-to-market vs. robustness priority: Under 'fast_mvp', defer non-critical Recommended practices and record them in TRADE-OFFS.
- BUS-06 Critical business capabilities: Mark which modules support critical capabilities.
- BUS-07 Build vs. buy: Isolate third-party dependencies behind anti-corruption layers.
- BUS-08 Post-delivery operating model: Produce runbooks for critical flows.; Automate repetitive operational tasks.
- BUS-09 Business data lifecycle: Define retention and disposal according to the data's role.
- BUS-10 Evolution / sunset plan: For 'long_term_platform', prioritize extensibility and API versioning.
- DATA-01 Data classification: Classify each dataset and propagate the tag to the store.
- DATA-02 Data model: Choose the store according to the model and access patterns.
- DATA-04 Consistency and integrity: Use ACID transactions where integrity is critical.
- DATA-06 Retention and disposal: Define retention per class and automate disposal.
- DATA-07 Privacy and sovereignty: Anonymize or pseudonymize where applicable and respect data residency.
- DATA-09 Backup and RPO: Define backup according to the tier and test restore periodically.
- INFRA-01 Hosting model: Choose the model according to sovereignty, latency and operating capacity.
- INFRA-02 Compute model: Choose according to the load pattern and the BUS-08 operational maturity.
- INFRA-04 RTO and recovery: Define and rehearse the recovery plan proportional to the RTO.
- INFRA-06 Security posture: Apply least privilege and segmentation per the DATA-01 classification.

## Guardrails (Recommended)
- APP-03 Internal communication style: Prefer a modular monolith unless criticality/complexity justify the cost of microservices.; Isolate external integrations with an anti-corruption layer.
- APP-05 Failure resilience: Apply an explicit timeout on every external call.; Use retry with exponential backoff and jitter.
- APP-06 Observability: Emit structured logs with a correlation ID.; Expose RED metrics and build dashboards.
- DATA-10 Integration and movement: Choose the mechanism according to latency and volume.
- INFRA-03 Availability topology: Size the topology to the SLO declared in NFR-01.
- INFRA-07 Network and exposure: Expose through the minimal necessary edge; add gateway/WAF and rate limit on public surfaces (T2+).
- INFRA-09 CI/CD and deploy strategy: Automate the pipeline and reduce release risk according to the tier.

## Out of scope
- APP-02 Domain modeling (Deferred) — see TRADE-OFFS.md
- APP-10 Extensibility (Deferred) — see TRADE-OFFS.md
- DATA-03 Volume and growth (Deferred) — see TRADE-OFFS.md
- DATA-05 Access patterns (Deferred) — see TRADE-OFFS.md
- DATA-08 Lineage, quality and governance (Deferred) — see TRADE-OFFS.md
- INFRA-05 Scalability (Deferred) — see TRADE-OFFS.md
- INFRA-08 IaC and change management (Deferred) — see TRADE-OFFS.md
- INFRA-10 Cost and sustainability (Deferred) — see TRADE-OFFS.md

---
*X-PRO.ai · catalog v1.1.0 · generator v1.1.0*
