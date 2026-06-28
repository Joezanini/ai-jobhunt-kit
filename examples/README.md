# Examples

Fictional starter data for the AI Job Hunt Kit pilot workflow.

## Required starter files

| File | `local-paths.json` key | Description |
|------|------------------------|-------------|
| [sample_resume.md](./sample_resume.md) | `base_resume` | ATS-friendly base resume (Alex Rivera) |
| [sample_role_reference.md](./sample_role_reference.md) | `current_role_reference` | Detailed current-role context |

## Supporting files

| File | Key | Description |
|------|-----|-------------|
| [sample_job_opportunities.md](./sample_job_opportunities.md) | `job_opportunities` | 2 fictional LinkedIn-style postings |
| [sample_contact.json](./sample_contact.json) | `contact` | Contact block for headers and PDF autolink |
| [sample_manifest.json](./sample_manifest.json) | — | Demo batch manifest (2 roles) |

## Getting started

1. Read [docs/STARTER_FILES.md](../docs/STARTER_FILES.md).
2. Copy `local-paths.example.json` → `local-paths.json` (points at these examples for dry run).
3. Follow [docs/END_TO_END_WORKFLOW.md](../docs/END_TO_END_WORKFLOW.md) step 1.

Replace fictional files with your own locally—never commit real PII to a public fork.
