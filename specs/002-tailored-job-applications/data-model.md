# Data Model: Batch Tailored Job Application Artifacts

**Feature**: `002-tailored-job-applications` | **Date**: 2026-06-27

This feature produces structured markdown intermediates, PDF deliverables, a batch manifest, and Google Drive artifacts. No database.

## Entity: JobOpportunity

Parsed from `sf_bay_area_job_opportunities.md`. One per in-scope role (20 total).

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `role_id` | string (slug) | yes | Unique; lowercase kebab-case; see research.md inventory |
| `company` | string | yes | As documented in source file |
| `title` | string | yes | Full role title |
| `location` | string | no | City/region if available |
| `work_model` | string | no | On-site, hybrid, remote |
| `salary_range` | string | no | Posted range or "Not posted" |
| `linkedin_url` | string (URL) | no | From Quick Links section |
| `summary` | string | yes | Job description summary text |
| `fit_notes` | string | no | "Why this fits" from source |
| `category` | enum | yes | `devrel`, `ai_enablement`, `partner_gtm`, `engineering`, `stretch`, `support_alt` |
| `warnings` | WarningFlag[] | no | See below |
| `keyword_targets` | string[] | yes | ≥5 terms extracted from summary for SC-005 |

### WarningFlag

| Value | Meaning |
|-------|---------|
| `citizenship_required` | Hard eligibility filter — flag in summary |
| `technical_stretch` | Domain gap noted in source |
| `thin_source_data` | Table-summary only |
| `recruiting_firm` | Agency posting |
| `salary_below_threshold` | Posted floor below $170K |

## Entity: SourceResume

Canonical facts from `joe_zanini_resume.md` + `cisco_role_reference.md` + `001-beast-ai-resume` clarifications.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `name` | string | yes | "ALEX RIVERA" |
| `contact` | ContactInfo | yes | Email, phone, LinkedIn, location |
| `experience` | ExperienceEntry[] | yes | Corrected dates (Qualys ends March 2022) |
| `education` | EducationEntry[] | yes | Matches source |
| `base_skills` | string[] | yes | From source resume |

**Immutable rules**: No fabricated employers, titles, dates, or degrees (FR-004).

## Entity: TailoredResume

Role-specific resume markdown. One per JobOpportunity.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `role_id` | string | yes | FK → JobOpportunity.role_id |
| `tagline` | string | yes | Descriptive phrases; role-aligned; not fabricated job title |
| `summary` | string | yes | 3–5 sentences; category-appropriate emphasis |
| `experience` | ExperienceEntry[] | yes | Same employers/dates as SourceResume; bullets reframed |
| `education` | EducationEntry[] | yes | Unchanged facts |
| `skills` | SkillGroup[] | yes | 2–4 groups; ordering varies by category |
| `local_md_path` | string | yes | Under `artifacts/002-tailored-job-applications/resumes/` |
| `local_pdf_path` | string | no | Set after PDF conversion |
| `drive_file_id` | string | no | Set after upload |
| `drive_file_name` | string | no | Per naming contract |

### ExperienceEntry / EducationEntry / SkillGroup

Same structure as `001-beast-ai-resume` data model. See [resume-markdown-schema.md](./contracts/resume-markdown-schema.md).

**Date rules** (FR-010):
- Webex: March 2022 – Present
- Qualys: June 2020 – March 2022
- Bonfire: March 2021 – August 2021
- Dor Technologies: July 2019 – March 2020

## Entity: CoverLetter

Role-specific cover letter markdown. One per JobOpportunity.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `role_id` | string | yes | FK → JobOpportunity.role_id |
| `company` | string | yes | Matches JobOpportunity |
| `title` | string | yes | Matches JobOpportunity |
| `date` | string | yes | Generation date |
| `body` | string | yes | 3–4 paragraphs; ≤1 page PDF |
| `local_md_path` | string | yes | Under `artifacts/.../cover-letters/` |
| `local_pdf_path` | string | no | Set after PDF conversion |
| `drive_file_id` | string | no | Set after upload |
| `drive_file_name` | string | no | Per naming contract |

## Entity: ApplicationArtifact

PDF deliverable in Google Drive.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `role_id` | string | yes | FK → JobOpportunity.role_id |
| `type` | enum | yes | `resume` or `cover_letter` |
| `file_name` | string | yes | Unique per naming contract |
| `drive_folder_id` | string | yes | Batch folder ID |
| `drive_file_id` | string | yes | From uploadFile response |
| `mime_type` | string | yes | `application/pdf` |
| `page_count` | integer | no | Resume 1–2; cover letter ≤1 |

## Entity: BatchRun

Single execution pass (full or partial).

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `batch_id` | string | yes | ISO timestamp or UUID |
| `started_at` | datetime | yes | |
| `completed_at` | datetime | no | |
| `drive_folder_name` | string | yes | Default: `Alex Rivera - SF Bay Area Applications 2026` |
| `drive_folder_id` | string | no | After createFolder |
| `role_statuses` | RoleStatus[] | yes | One per targeted role |

### RoleStatus

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `role_id` | string | yes | |
| `status` | enum | yes | `pending`, `generated`, `uploaded`, `failed`, `skipped` |
| `resume_pdf` | string | no | Drive file name or path |
| `cover_letter_pdf` | string | no | Drive file name or path |
| `error` | string | no | If failed |
| `warnings` | WarningFlag[] | no | Copied from JobOpportunity |

## Entity: DriveFolder

Google Drive container for batch.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `name` | string | yes | `Alex Rivera - SF Bay Area Applications 2026` |
| `folder_id` | string | yes | From createFolder |
| `artifact_count` | integer | yes | Target: 40 on full success |

## Relationships

```text
SourceResume ──tailors──► TailoredResume (×20)
JobOpportunity (1) ──► (1) TailoredResume
JobOpportunity (1) ──► (1) CoverLetter
TailoredResume ──converts──► ApplicationArtifact (resume PDF)
CoverLetter ──converts──► ApplicationArtifact (cover_letter PDF)
BatchRun ──tracks──► RoleStatus (×20)
DriveFolder ──contains──► ApplicationArtifact (×40)
```

## State Transitions (per role)

```text
pending → generated (markdown written)
generated → uploaded (PDFs in Drive)
generated → failed (conversion or upload error)
failed → generated (re-run FR-012)
uploaded → uploaded (re-run with version suffix if collision)
```

## Validation Rules Summary

| Rule ID | Entity | Check |
|---------|--------|-------|
| V-001 | TailoredResume | Every bullet traceable to SourceResume or cisco_role_reference |
| V-002 | TailoredResume | ≥5 keyword_targets appear in natural context |
| V-003 | TailoredResume | PDF 1–2 pages |
| V-004 | CoverLetter | Names company + role; no contradiction with resume |
| V-005 | CoverLetter | PDF ≤1 page |
| V-006 | ApplicationArtifact | file_name unique across batch |
| V-007 | BatchRun | 20/20 roles `uploaded` on full success (SC-001) |
| V-008 | All | Qualys/Webex dates corrected (FR-010) |
