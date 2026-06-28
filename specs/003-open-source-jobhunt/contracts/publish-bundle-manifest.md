# Contract: Publish Bundle Manifest

**Feature**: `003-open-source-jobhunt` | **Version**: 1.0

Allowlist of paths copied from `JOBHUNT/` into `export/ai-jobhunt-kit/` for the public GitHub repository. All entries are subject to [sanitization-policy.md](./sanitization-policy.md) transforms.

## Root files

| Source | Staging destination | Notes |
|--------|---------------------|-------|
| (generated) | `README.md` | Per readme-outline contract |
| (generated) | `LICENSE` | MIT |
| (generated) | `local-paths.example.json` | Fictional paths |
| (generated) | `.gitignore` | Public-repo appropriate ignores |
| `docs/PUBLISH_CHECKLIST.md` | `docs/PUBLISH_CHECKLIST.md` | Contributor gate |

## Examples (generated or copied sanitized)

| Staging path | Notes |
|--------------|-------|
| `examples/sample_resume.md` | Fictional persona |
| `examples/sample_job_opportunities.md` | 2 roles minimum |
| `examples/sample_role_reference.md` | Generic supplemental pattern |
| `examples/sample_contact.json` | Fictional contact |
| `examples/sample_manifest.json` | 2-role demo manifest |

## Spec Kit configuration

| Source glob | Staging | Transform |
|-------------|---------|-----------|
| `.specify/extensions.yml` | same | none |
| `.specify/extensions/**` | same | none |
| `.specify/templates/**` | same | none |
| `.specify/workflows/**` | same | none |
| `.specify/scripts/bash/**` | same | none |
| `.specify/feature.json` | **exclude** | Maintainer-specific |
| `.specify/init-options.json` | same | none |

## Cursor agent assets

| Source glob | Staging | Transform |
|-------------|---------|-----------|
| `.cursor/skills/speckit-*/**` | same | none |
| `.cursor/rules/specify-rules.mdc` | same | Point to generic plan or 003 plan |
| `.cursor/rules/public-facing-grammar.mdc` | same | Depersonalize |
| `.cursor/rules/pdf-clickable-links.mdc` | same | Depersonalize examples |

## Specifications (sanitized)

| Source | Staging | Transform |
|--------|---------|-----------|
| `specs/001-beast-ai-resume/**` | same | Redact author name in prose |
| `specs/002-tailored-job-applications/contracts/**` | same | Keep contracts generic |
| `specs/002-tailored-job-applications/data-model.md` | same | Replace SourceResume example name |
| `specs/002-tailored-job-applications/quickstart.md` | same | Point to `examples/` + local-paths |
| `specs/003-open-source-jobhunt/**` | same | This feature docs |
| `specs/002-tailored-job-applications/research.md` | **exclude** | Contains real 20-role inventory |
| `specs/002-tailored-job-applications/tasks.md` | **exclude** | Maintainer task list |

## Batch tooling

| Source | Staging | Transform |
|--------|---------|-----------|
| `artifacts/002-tailored-job-applications/batch/convert_to_pdf.py` | `scripts/batch/convert_to_pdf.py` | Depersonalize phone regex; read contact path from arg |
| `artifacts/002-tailored-job-applications/batch/README.md` | `scripts/batch/README.md` | Generic paths |
| `artifacts/002-tailored-job-applications/batch/GRAMMAR_STYLE.md` | `docs/GRAMMAR_STYLE.md` | none |

## Explicitly excluded from bundle

Everything on the sanitization denylist plus:
- Entire `artifacts/` tree except scripts noted above
- Root personal markdown sources
- `joe_zanini_resume.md`, `sf_bay_area_job_opportunities.md`, `cisco_role_reference.md`
- Any `*.pdf`, `__pycache__/`, `.DS_Store`

## Expected file count

Approximately 50–80 files. Build script MUST report actual count and fail if zero denylist hits but count &lt; 40 (incomplete bundle).
