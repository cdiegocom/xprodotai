# Changelog — x-pro-catalog

Every project pins a version in `x-pro.lock`. This changelog is what you read before
running `upgrade`: it tells you whether the new version can change your artifacts' recommendations.

Format follows [Keep a Changelog](https://keepachangelog.com) and semver.

## [Unreleased]

## [1.1.0] — {{ DATE }}
### Changed (refines recommendations — may change artifacts on upgrade)
- Gating v1.1: new `required_if` field (answer-driven gate) and `deferrable`
  (controls the `fast_mvp` modulation). See `calibration/CALIBRATION.md`.

### Upgrade notes
- `fast_mvp` projects: practices with `deferrable: false` are no longer downgraded
  (e.g. modular monolith, logs, basic CI/CD return to Recommended).
- Practices with `required_if` become Required when the answer triggers them
  (e.g. `DATA-03` at big-data volume). Review via fixtures before bumping the lock.

## [1.0.0] — {{ DATE }}
### Added
- Tier engine (Layer 0): 9 questions, Criticality × Complexity matrix, override ratchet.
- Application battery (APP-01..10) with structured `do/dont/example/verification` directives.
- Security baseline (SEC) driven by classification + security tier.

### Upgrade notes
- First release. No migrations.

---
*X-PRO.ai · version 1.1.0*
