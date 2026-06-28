# Quickstart: Validate Batch Tailored Job Application Artifacts

**Feature**: `002-tailored-job-applications`

## Prerequisites

- Source files at project root:
  - `sf_bay_area_job_opportunities.md`
  - `joe_zanini_resume.md`
  - `cisco_role_reference.md` (supplemental Webex facts)
- Google Drive MCP server authenticated (`authGetStatus` returns connected)
- PDF conversion tool (one of):
  - `brew install pandoc` (recommended)
  - `npx md-to-pdf <file.md>` (no global install)
- Design contracts in [contracts/](./contracts/)

## Setup

```bash
cd /Users/joezanini/JOBHUNT
mkdir -p artifacts/002-tailored-job-applications/{resumes,cover-letters,pdf,batch}
```

Initialize manifest with all 20 roles per [job-opportunity-manifest-schema.md](./contracts/job-opportunity-manifest-schema.md) and [research.md](./research.md) R1 table.

## Validation Scenarios

### 1. Drive access (prerequisite)

Call Drive MCP `authGetStatus`.

**Expected**: Authenticated; Drive scope available.

### 2. Create batch folder

Call `createFolder` with name `Alex Rivera - SF Bay Area Applications 2026`.

**Expected**: Folder ID returned; record in `batch/manifest.json` as `drive_folder_id`.

### 3. Single-role pilot (recommended before full batch)

Pick `fractional-ai-devrel`:

1. Write `artifacts/002-tailored-job-applications/resumes/fractional-ai-devrel.md` per [resume-markdown-schema.md](./contracts/resume-markdown-schema.md)
2. Write `artifacts/002-tailored-job-applications/cover-letters/fractional-ai-devrel.md` per [cover-letter-schema.md](./contracts/cover-letter-schema.md)
3. Convert both to PDF (pandoc or npx md-to-pdf)
4. Upload via `uploadFile` with names from [file-naming-convention.md](./contracts/file-naming-convention.md)

**Expected**: 2 PDFs in Drive folder; openable; resume 1–2 pages; cover letter ≤1 page.

### 4. Manifest completeness

```bash
# After manifest is created
test -f artifacts/002-tailored-job-applications/batch/manifest.json
```

**Expected**: JSON contains exactly 20 role entries with unique `role_id` values.

### 5. Employment date consistency (FR-010)

Spot-check any 3 generated resumes:

| Role | Dates |
|------|-------|
| Webex | March 2022 – Present |
| Qualys | June 2020 – March 2022 |

**Expected**: Only Webex shows "Present."

### 6. Keyword coverage (SC-005)

For pilot role, confirm ≥5 `keyword_targets` from manifest appear naturally in resume body.

```bash
rg -i 'developer relations|technical content|open source|conferences|engineering' \
  artifacts/002-tailored-job-applications/resumes/fractional-ai-devrel.md
```

**Expected**: Contextual usage; not a keyword footer.

### 7. Traceability (SC-004)

Review pilot resume bullets against `joe_zanini_resume.md` and `cisco_role_reference.md`.

**Expected**: Zero fabricated claims.

### 8. File naming uniqueness (SC-002)

List Drive folder via `listFolder` after pilot or full batch.

**Expected**: All names match `Zanini_Joe_{Resume|CoverLetter}_{CompanySlug}_{RoleSlug}.pdf`; no duplicates.

### 9. Anthropic multi-role disambiguation

After generating all 3 Anthropic roles, confirm 6 distinct PDFs with role-specific slugs (not `Anthropic_Resume.pdf` alone).

**Expected**: Three unique `RoleSlug` values in file names.

### 10. Full batch completion (SC-001)

After all 20 roles processed:

**Expected**:
- 40 PDFs in Drive folder
- `batch/summary.md` lists each role as `uploaded` or `failed` with warnings
- Manifest `status` fields updated

### 11. Partial re-run (FR-012)

Set one role to `failed` in manifest; re-process only that `role_id`.

**Expected**: Only that role's 2 PDFs regenerated; other 38 files untouched.

## Pass Criteria

- Pilot (scenarios 1–7) passes → proceed with full batch
- Full batch (scenarios 8–10) passes → ready for Joe's review before LinkedIn submission
- Re-run (scenario 11) passes → batch tooling is production-ready

## References

- [spec.md](./spec.md) — requirements and success criteria
- [data-model.md](./data-model.md) — entities and validation rules
- [research.md](./research.md) — role inventory, PDF pipeline, Drive integration
- [plan.md](./plan.md) — implementation outline
