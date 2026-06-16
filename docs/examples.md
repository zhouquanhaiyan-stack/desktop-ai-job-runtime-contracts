# Examples

This document describes the example manifests and runner included in this
repository. These examples demonstrate the job manifest contract and the
`run_fake_job.py` runner without requiring any real AI infrastructure.

> **Important:** All examples are dry-run contract demonstrations. No real AI
> inference is performed. Output artifacts are small text files produced by
> the `FakeRuntimeAdapter` for contract testing purposes.

---

## Audio example

**Manifest:** `examples/fake_audio_job.json`

A minimal audio-processing job with a single WAV input. This is the default
manifest used when `run_fake_job.py` is invoked without arguments.

- `job_id`: `fake-audio-job-001`
- `job_type`: `audio`
- Input media type: `audio/wav`

## Image example

**Manifest:** `examples/fake_image_job.json`

An image-processing job with a single PNG input. Pass this manifest explicitly
to the runner to exercise the same pipeline with a different `job_type`.

- `job_id`: `fake-image-job-001`
- `job_type`: `image`
- Input media type: `image/png`

## Text example

**Manifest:** `examples/fake_text_job.json`

A text-processing job with a single plain-text input. This example includes
a `metadata.purpose` field to illustrate how custom metadata can be attached
to a job manifest.

- `job_id`: `fake-text-job-001`
- `job_type`: `text`
- Input media type: `text/plain`
- Metadata: `purpose = "contract smoke example"`

---

## Running examples

All examples are run from the repository root using the same runner script:

```bash
# Audio (default)
python examples/run_fake_job.py

# Image
python examples/run_fake_job.py examples/fake_image_job.json

# Text
python examples/run_fake_job.py examples/fake_text_job.json
```

The runner accepts an optional manifest path argument. When no argument is
given, it defaults to `examples/fake_audio_job.json`.

---

## Expected outputs

Each run creates an output directory under `examples/out/<job-id>/` containing:

| File                  | Description                              |
|-----------------------|------------------------------------------|
| `result_manifest.json`| Final manifest with updated status and artifacts |
| `execution_trace.json`| Event-level trace of the job lifecycle   |

Typical output:

```
  job_id        : fake-text-job-001
  job_type      : text
  status        : succeeded
  artifact count: 2
  result_manifest: .../out/fake-text-job-001/result_manifest.json
  execution_trace: .../out/fake-text-job-001/execution_trace.json

  Trace events:
    [init] Loaded manifest fake-text-job-001
    [validate] Validated manifest
    [execute] Running fake adapter for text job
    [finalize] Job complete
```

---

## Notes

- **No real AI inference** — The `FakeRuntimeAdapter` produces deterministic
  placeholder artifacts without calling any external model.
- **No external dependencies** — The runner and all examples use only the
  Python standard library.
- **Non-production** — These examples are designed for contract validation,
  CI smoke tests, and development experimentation. They should not be used
  in production pipelines.