# X-PRO.ai — Extreme Software Process for AI Driven-Development

A library of artifacts that defines **how an AI agent should build this project**,
calibrated to real criticality and complexity (not the "best of all worlds").

Every artifact is generated from the answers to the functional-question batteries and the
**Tier** computed in Layer 0. The Tier modulates each practice: what is `Required` in a
critical system may be `Discarded` in a PoC — and the reason is always recorded.

## How to instantiate

1. Answer Layer 0 and the 4 batteries (Business, Application, Data, Infrastructure).
2. The generator fills each `{{ PLACEHOLDER }}` and resolves the status of every decision block.
3. Version this folder in the project repository.
4. Point the AI agent (Claude Code, Cursor, Copilot) at `AI-AGENT-RULES.md`.

## File map

| File | Role |
|---|---|
| `x-pro-manifest.yaml` | Machine-readable index: version, tiers, artifact list |
| `x-pro.lock` | Pins the global catalog version (reproducibility) |
| `00-PROJECT-PROFILE.md` | Layer 0 output: scores, global and per-dimension Tier, overrides, conflicts |
| `01-BUSINESS-CONSTRAINTS.md` | Business layer (clones the layer template) |
| `02-APPLICATION-GUIDELINES.md` | Application layer — **canonical** layer template |
| `03-DATA-GUIDELINES.md` | Data layer (clones the layer template) |
| `04-INFRASTRUCTURE-GUIDELINES.md` | Infrastructure layer (clones the layer template) |
| `NFR.md` | Non-functional targets: SLO, RTO/RPO, budgets, error budget |
| `SECURITY-BASELINE.md` | Minimum controls from classification + override |
| `TRADE-OFFS.md` | Record of what was `Deferred`/`Discarded` and why |
| `DEFINITION-OF-DONE.md` | Gate checklist, per dimension and tier |
| `AI-AGENT-RULES.md` | Imperative operative rules the agent reads to build within the rails |
| `ADR/` | Architecture Decision Records, one per relevant decision |

## Conventions (apply to all files)

- **Placeholders:** `{{ UPPER_SNAKE }}` = value filled by the generator.
- **Generation notes:** `<!-- xpro: instruction -->` = guidance for whoever instantiates.
- **Status:** `Required` · `Recommended` · `Deferred` · `Discarded`.
- **IDs:** `BUS-NN`, `APP-NN`, `DATA-NN`, `INFRA-NN`, `NFR-NN`, `SEC-NN`, `ADR-NNNN`.
- **Tier dimensions:** `reliability`, `security`, `performance`, `cost`, `operational`, `sustainability`.
- **References:** AWS Well-Architected · Azure WAF · Google SRE · 12-factor · DORA.

> The source of truth for the Tier is `00-PROJECT-PROFILE.md`. No file should contradict it.

---
*X-PRO.ai · version 1.1.0*
