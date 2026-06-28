# Data Model: Resume Deliverables

**Feature**: `001-beast-ai-resume` | **Date**: 2026-06-25

This feature produces structured markdown documents, not a database. Entities below define the document schema and validation rules.

## Entity: TailoredResume

Primary deliverable at `joe_zanini_resume_beast_ai_enablement.md`.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `name` | string (H1) | yes | Must be "ALEX RIVERA" |
| `tagline` | string (plain line) | yes | Descriptive phrases only; not a job title |
| `contact` | string (single line) | yes | Email, LinkedIn, phone, location from source resume; no relocation text |
| `summary` | string (3–5 sentences) | yes | Builder-first enablement; moderate AI language |
| `experience` | ExperienceEntry[] | yes | Reverse chronological; dates consistent |
| `education` | EducationEntry[] | yes | Matches source resume facts |
| `skills` | SkillGroup[] | yes | Three groups: AI & Automation, Engineering, Enablement |

### ExperienceEntry

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `title` | string | yes | Exact employer title from source or clarified |
| `company` | string | yes | Employer name |
| `dates` | string | yes | Format `Month YYYY – Month YYYY` or `Present` |
| `bullets` | string[] | yes | 4–7 bullets for primary role; 3–5 for others; each traceable to source |

**Ordering**: Webex → Qualys → Bonfire → Dor Technologies

**Date rules**:
- Webex: March 2022 – Present
- Qualys: June 2020 – March 2022
- Bonfire: March 2021 – August 2021 (overlaps Qualys part-time—acceptable)
- Dor: July 2019 – March 2020

### EducationEntry

| Field | Type | Required |
|-------|------|----------|
| `degree` | string | yes |
| `institution` | string | yes |
| `graduation` | string | yes |

### SkillGroup

| Field | Type | Required |
|-------|------|----------|
| `name` | string | yes |
| `items` | string[] | yes |

## Entity: AIWorkExamplesAnnex

Companion deliverable at `ai_work_examples_beast.md`.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `examples` | WorkExample[2] | yes | Exactly two entries |

### WorkExample

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `title` | string | yes | Short name |
| `description` | string | yes | 2–4 sentences; honest scope |
| `reference` | string | yes | URL or repo path verifiable before submission |
| `relevance` | string | yes | 1–2 sentences tying to Beast role |

**Fixed examples** (from clarifications):
1. Webex Python SDK / technical content
2. Spec Kit / agentic tooling (this repository)

## Entity: KeywordCoverageMap

Derived validation artifact (not a separate file unless needed at implement time).

Tracks SC-002: ≥12 of 15 core posting terms present naturally in TailoredResume body.

## Relationships

```text
SourceResume ──transforms──▶ TailoredResume
TargetJobPosting ──informs──▶ TailoredResume
TargetJobPosting ──informs──▶ AIWorkExamplesAnnex
TailoredResume ──submitted-with──▶ AIWorkExamplesAnnex
```

## State Transitions

```text
[source resume] → [draft tailored resume] → [keyword/traceability check] → [PDF validation] → [ready to submit]
```
