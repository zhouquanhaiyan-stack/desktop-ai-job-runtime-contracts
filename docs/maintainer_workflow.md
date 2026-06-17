# Maintainer Workflow

## Purpose

This document records the minimal maintenance process project maintainers should follow before and after making changes to documentation, specification, examples, or runtime contracts. Following these steps keeps the project reproducible, dependency-free, and easy to review.

## Before Making Changes

* Confirm the repository is on the `main` branch or a dedicated working branch.
* Review the current README, CHANGELOG, and relevant docs before editing.
* Keep the project dependency-free unless a future proposal explicitly changes that rule.
* Avoid private paths, credentials, production services, or external API assumptions.

## Local Validation Checklist

After making changes, run the following commands from the repository root to verify correctness:

```bash
python -m py_compile src/desktop_ai_job_runtime_contracts/*.py
python -m unittest discover -s tests -v
python examples/run_fake_job.py
python examples/run_fake_job.py examples/fake_image_job.json
python examples/run_fake_job.py examples/fake_text_job.json
```

## After Committing

* Push changes and any new tags to the remote repository.
* Verify the GitHub Actions CI badge shows a passing build.
* Update the release notes if the change is user-facing or affects the contract surface.
