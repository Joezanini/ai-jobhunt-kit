# Contract: PDF File Naming Convention

**Version**: 1.0.0 | **Feature**: `002-tailored-job-applications`

## Purpose

Defines deterministic, unique file names for all PDF deliverables (FR-008, SC-002, SC-003).

## Pattern

```
Zanini_Joe_{DocumentType}_{CompanySlug}_{RoleSlug}.pdf
```

| Component | Values | Rules |
|-----------|--------|-------|
| `DocumentType` | `Resume`, `CoverLetter` | PascalCase; exactly one of these |
| `CompanySlug` | From manifest `company_slug` | No spaces; alphanumeric |
| `RoleSlug` | From manifest `role_slug` | PascalCase concatenation |

## Examples

| role_id | Resume file name |
|---------|------------------|
| `anthropic-claude-code-specialist` | `Zanini_Joe_Resume_Anthropic_TechnicalSpecialistClaudeCode.pdf` |
| `fractional-ai-devrel` | `Zanini_Joe_Resume_FractionalAI_DeveloperRelationsEngineer.pdf` |
| `kinora-devadvocate` | `Zanini_Joe_Resume_KinoraGroup_DeveloperAdvocate.pdf` |

Cover letters substitute `CoverLetter` for `Resume`.

## Collision Handling

If `uploadFile` or `listFolder` detects an existing file with the same name in the batch folder:

1. Append `_YYYYMMDD` before `.pdf` (e.g., `_20260627`)
2. If still colliding, append `_v2`, `_v3`, etc.
3. Record final name in manifest `role_statuses`

## Local Staging Paths

| Artifact | Local path |
|----------|------------|
| Resume markdown | `artifacts/002-tailored-job-applications/resumes/{role_id}.md` |
| Resume PDF | `artifacts/002-tailored-job-applications/pdf/{role_id}_resume.pdf` |
| Cover letter markdown | `artifacts/002-tailored-job-applications/cover-letters/{role_id}.md` |
| Cover letter PDF | `artifacts/002-tailored-job-applications/pdf/{role_id}_cover_letter.pdf` |

Local PDF names may differ from Drive names; Drive names MUST follow the pattern above.
