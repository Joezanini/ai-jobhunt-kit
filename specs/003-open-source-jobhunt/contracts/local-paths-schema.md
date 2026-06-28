# Contract: Local Paths Schema

**Feature**: `003-open-source-jobhunt` | **Version**: 1.0

JSON schema for `local-paths.json` (gitignored) and `local-paths.example.json` (tracked in public repo).

## File shape

```json
{
  "$schema": "local-paths-v1",
  "base_resume": "path/to/base_resume.md",
  "job_opportunities": "path/to/job_opportunities.md",
  "current_role_reference": "path/to/current_role_reference.md",
  "contact": "path/to/contact.json",
  "artifacts_root": "path/to/artifacts/feature-id/",
  "candidate_name": {
    "first": "Alex",
    "last": "Rivera"
  },
  "drive_folder_name": "Alex Rivera - Job Applications 2026"
}
```

## Field definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `$schema` | string | yes | Literal `local-paths-v1` |
| `base_resume` | string | yes | Canonical resume markdown |
| `job_opportunities` | string | yes | Job list markdown |
| `current_role_reference` | string | yes | Detailed description of current role (employer scope, projects, honest title variants) |
| `contact` | string | yes | Contact JSON for headers and PDF autolink |
| `artifacts_root` | string | yes | Root for resumes/, cover-letters/, pdf/, batch/ |
| `candidate_name.first` | string | yes | Used in PDF file naming |
| `candidate_name.last` | string | yes | Used in PDF file naming |
| `drive_folder_name` | string | no | Optional Drive folder label |

Paths may be project-relative (preferred) or absolute.

## Required starter inputs (before job search)

Adopters and maintainers MUST have these two files configured before LinkedIn discovery or batch tailoring:

1. **`base_resume`** — Up-to-date resume markdown (contact, experience, education, skills).
2. **`current_role_reference`** — Detailed current-role document: employer context, honest title variants, projects, links, and scope not fully captured on the one-page resume.

Both paths are set in `local-paths.json`. Public repo ships fictional versions under `examples/`.

## Maintainer instance (not committed)

```json
{
  "$schema": "local-paths-v1",
  "base_resume": "joe_zanini_resume.md",
  "job_opportunities": "sf_bay_area_job_opportunities.md",
  "current_role_reference": "cisco_role_reference.md",
  "contact": "artifacts/002-tailored-job-applications/batch/contact.json",
  "artifacts_root": "artifacts/002-tailored-job-applications/",
  "candidate_name": { "first": "Joe", "last": "Zanini" },
  "drive_folder_name": "Alex Rivera - SF Bay Area Applications 2026"
}
```

## Adopter instance (from example)

```json
{
  "$schema": "local-paths-v1",
  "base_resume": "examples/sample_resume.md",
  "job_opportunities": "examples/sample_job_opportunities.md",
  "current_role_reference": "examples/sample_role_reference.md",
  "contact": "examples/sample_contact.json",
  "artifacts_root": "artifacts/pilot/",
  "candidate_name": { "first": "Alex", "last": "Rivera" },
  "drive_folder_name": "Alex Rivera - Job Applications 2026"
}
```

## Resolution rules

1. If `local-paths.json` exists at repo root, agents and scripts MUST use it.
2. Else if `local-paths.example.json` exists, copy to `local-paths.json` and prompt user to customize.
3. File naming contract reads `candidate_name` from this config—not hard-coded names in skills.

## Git rules

- `local-paths.json` → **gitignored**
- `local-paths.example.json` → **tracked** in public repo only (sanitized example)
