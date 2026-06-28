# Business — guidelines

<!-- GENERATED. Edit the catalog and regenerate. -->

### [BUS-01] Success metric (North Star) — **Required**
- Do: Instrument the chosen metric explicitly from the MVP onward.
- Don't: Do not optimize dimensions that don't move the primary metric.
- Verification: The primary metric is measurable in production.

### [BUS-02] Governance model — **Required**
- Do: Record relevant decisions as ADRs.; Define who approves architecture changes.
- Don't: Do not make a structural decision without an ADR in a T2+ project.
- Verification: Architecture decisions have a traceable ADR.

### [BUS-03] Compliance obligations — **Required**
- Do: List the concrete obligations: minimum retention, residency, right to erasure.
- Don't: Do not treat compliance as an optional backlog item.
- Verification: Each obligation has a matching control in SECURITY-BASELINE.

### [BUS-04] Revenue model and cost sensitivity — **Required**
- Do: Set a cost ceiling and instrument spend per unit of value.
- Don't: Do not oversize infrastructure without revenue justification.
- Verification: A budget and cost visibility exist (basic FinOps).

### [BUS-05] Time-to-market vs. robustness priority — **Required**
- Do: Under 'fast_mvp', defer non-critical Recommended practices and record them in TRADE-OFFS.
- Don't: Do not use 'fast_mvp' to skip Required controls — those never yield.
- Verification: Speed-driven deferrals are recorded with a review trigger.

### [BUS-06] Critical business capabilities — **Required**
- Do: Mark which modules support critical capabilities.
- Don't: Do not level every module to the same rigor if capabilities differ.
- Verification: Critical modules have an effective tier equal to or higher than ancillary ones.

### [BUS-07] Build vs. buy — **Required**
- Do: Isolate third-party dependencies behind anti-corruption layers.
- Don't: Do not couple business logic directly to a vendor's API.
- Verification: Swapping a vendor does not require rewriting the domain.

### [BUS-08] Post-delivery operating model — **Required**
- Do: Produce runbooks for critical flows.; Automate repetitive operational tasks.
- Don't: Do not leave operations dependent on one person's tacit knowledge.
- Verification: Critical flows have runbooks and operational toil is mapped.

### [BUS-09] Business data lifecycle — **Required**
- Do: Define retention and disposal according to the data's role.
- Don't: Do not treat a system-of-record as lightly as ephemeral data.
- Verification: A retention/disposal policy consistent with the data's role exists.

### [BUS-10] Evolution / sunset plan — **Required**
- Do: For 'long_term_platform', prioritize extensibility and API versioning.
- Don't: Do not invest in extensibility for a 'throwaway_after_validation' system.
- Verification: The level of extensibility is consistent with the declared horizon.


---
*X-PRO.ai · catalog v1.1.0 · generator v1.1.0*
