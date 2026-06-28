# Application — guidelines

<!-- GENERATED. Edit the catalog and regenerate. -->

### [APP-01] Presentation pattern — **Required**
- Do: Adopt the pattern that fits the interaction: MVC (server-rendered), MVVM (SPA+API), hexagonal (headless), pipeline (batch/worker).
- Don't: Do not put business logic in the presentation layer.
- Verification: The presentation layer contains no business logic.

### [APP-02] Domain modeling — **Deferred**
- Do: Use a light Domain Model: entities with their own invariants.
- Don't: Avoid aggregates and bounded contexts if the domain isn't rich.
- Verification: Invariants live in entities, not in scattered ifs.
- Trade-off: Full tactical DDD discarded. -> TRADE-OFFS.md

### [APP-03] Internal communication style — **Recommended**
- Do: Prefer a modular monolith unless criticality/complexity justify the cost of microservices.; Isolate external integrations with an anti-corruption layer.
- Don't: Do not fragment into microservices without operational maturity (BUS-08).
- Verification: Module boundaries are explicit; external integrations have an ACL.

### [APP-04] Consistency — **Required**
- Do: Use transactions where integrity is critical; saga/outbox for consistency across services.
- Don't: Do not distribute a transaction without a pattern — avoid fragile two-phase commit.
- Verification: Multi-step operations have a guarantee (transaction or saga).

### [APP-05] Failure resilience — **Recommended**
- Do: Apply an explicit timeout on every external call.; Use retry with exponential backoff and jitter.
- Don't: Do not add a circuit breaker — deferred at this tier.
- Verification: Every external call has a timeout and retry policy.

### [APP-06] Observability — **Recommended**
- Do: Emit structured logs with a correlation ID.; Expose RED metrics and build dashboards.
- Verification: Key metrics have a dashboard.

### [APP-07] AuthN / AuthZ — **Required**
- Do: Centralize identity (OIDC) and enforce authorization at the right point (gateway or service).; In multi-tenant, isolate data per tenant.
- Don't: Do not implement home-grown identity or cryptography.
- Verification: Access is authenticated and authorized; tenants isolated.

### [APP-08] Testing strategy — **Required**
- Do: Cover the critical path with unit tests.; Add integration tests and an agreed minimum coverage.
- Verification: Integration covers the main flows.

### [APP-09] Configuration and secrets — **Required**
- Do: Read config from environment variables; keep secrets in a vault.; Use feature flags to decouple deploy from release when useful.
- Don't: Never commit a secret to the repository.
- Verification: No secret in code; configuration externalized.

### [APP-10] Extensibility — **Deferred**
- Do: For a product/platform, use ports & adapters and version the public API.; Define a backward-compatibility policy.
- Don't: Do not invest in extensibility for a throwaway system.
- Verification: Extension points and versioning fit the BUS-10 horizon.
- Trade-off: Ports & adapters / API versioning deferred. -> TRADE-OFFS.md


---
*X-PRO.ai · catalog v1.1.0 · generator v1.1.0*
