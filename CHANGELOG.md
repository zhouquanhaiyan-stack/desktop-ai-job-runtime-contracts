# Changelog
## [0.1.1] - Unreleased

### Added

- GitHub Actions CI for syntax checks, unit tests, and example execution.
- Issue templates for bug reports, feature requests, and documentation improvements.
- Pull request template for dependency-free contract changes.


## 0.1.0 (2026-06-17)

- Initial public release
- Core contracts: JobType, JobStatus, ArtifactKind, RuntimeCapability, JobInput, JobArtifact, RuntimeAdapterInfo
- Job manifest: serialization (JSON), deserialization, file I/O, and validation
- Runtime adapter: abstract BaseRuntimeAdapter + FakeRuntimeAdapter with trace events and artifact generation
- Execution trace: event-level recording with timestamps and metadata
- Export guard: sample free/plus/pro policy stub
- Runner: top-level run_job orchestration
- Examples: fake_audio_job, fake_image_job, run_fake_job.py
- Tests: manifest, adapter, trace, export_guard (unittest)
- Documentation: architecture, job_manifest, adapter_contract, execution_trace, export_guard

