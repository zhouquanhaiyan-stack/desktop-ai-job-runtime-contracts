# Changelog

## [Unreleased]

## [0.1.0] - 2026-06-17

### Added

* Initial dependency-free runtime contract package.
* Job manifest schema and validation helpers.
* Runtime adapter boundary with a fake adapter for CI-safe execution.
* Execution trace model with serializable trace events.
* Export guard demonstration policy.
* Audio, image, and text fake job examples.
* Unit tests for manifests, adapters, traces, export guard behavior, and examples.
* GitHub Actions CI across Python 3.10, 3.11, and 3.12.
* Issue templates and pull request template for open-source maintenance.

### Changed

* Example runner supports an optional manifest path argument.
* Test files now set their own local src import path for reliable unittest discovery.
