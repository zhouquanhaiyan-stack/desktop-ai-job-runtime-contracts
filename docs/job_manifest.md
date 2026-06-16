# Job Manifest

## Overview

The job manifest is the primary input and output document for the runtime contract system. It describes what work to do (inputs, type) and captures what happened (status, artifacts).

## JobManifest fields

| Field       | Type                   | Required | Description                             |
|-------------|------------------------|----------|-----------------------------------------|
| job_id      | str                    | yes      | Unique identifier for the job           |
| job_type    | JobType                | yes      | AUDIO, IMAGE, VIDEO, TEXT, or GENERIC  |
| inputs      | list[JobInput]         | yes      | At least one input must be provided     |
| output_dir  | str                    | yes      | Directory for output artifacts          |
| status      | JobStatus              | yes      | PENDING, RUNNING, SUCCEEDED, FAILED, CANCELED |
| artifacts   | list[JobArtifact]      | no       | Created by the runtime adapter          |
| metadata    | dict[str, str]         | no       | Arbitrary key-value metadata            |

## JSON example

```json
{
  "job_id": "fake-audio-job-001",
  "job_type": "audio",
  "inputs": [
    {
      "input_id": "in-001",
      "path": "samples/input.wav",
      "media_type": "audio/wav",
      "metadata": {}
    }
  ],
  "output_dir": "examples/out/fake-audio-job-001",
  "status": "pending",
  "artifacts": [],
  "metadata": {}
}
```

## JobInput

| Field      | Type             | Description                              |
|------------|------------------|------------------------------------------|
| input_id   | str              | Unique identifier within the manifest    |
| path       | str              | Path to the input file                   |
| media_type | str              | MIME type of the input                   |
| metadata   | dict[str, str]   | Optional key-value descriptors           |

## JobArtifact

| Field      | Type             | Description                              |
|------------|------------------|------------------------------------------|
| artifact_id| str              | Unique identifier for this artifact      |
| kind       | ArtifactKind     | PREVIEW, EXPORT, LOG, TRACE, or MANIFEST |
| path       | str              | Output path for the artifact file        |
| media_type | str              | MIME type of the artifact                |
| metadata   | dict[str, str]   | Optional key-value descriptors           |

## Validation rules

The `validate_manifest()` function enforces:

- `job_id` must not be empty
- `job_type` must be a valid JobType enum value
- At least one input is required
- Every input must have non-empty `input_id`, `path`, and `media_type`
- `output_dir` must not be empty
- `status` must be a valid JobStatus enum value
