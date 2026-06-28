# Implementation Plan: Batch Tailored Job Application Artifacts

**Branch**: `002-tailored-job-applications` | **Date**: 2026-06-27 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/002-tailored-job-applications/spec.md`

## Summary

Process all 20 job opportunities in `sf_bay_area_job_opportunities.md` and produce tailored, ATS-friendly resumes and role-specific cover letters for Alex Rivera. Each role yields two PDFs uploaded to a dedicated Google Drive folder via the Drive MCP server, with position-specific file naming. Implementation is agent-driven content authoring plus a manifest-tracked batch pipeline: markdown intermediates → local PDF conversion → Drive upload, with partial re-run support and a completion summary.

## Technical Context

**Language/Version**: Markdown (GitHub-flavored); JSON manifest; PDF via Pandoc or `npx md-to-pdf`

**Primary Dependencies**:
- `sf_bay_area_job_opportunities.md` — role inventory and tailoring context
- `joe_zanini_resume.md` — canonical resume facts
- `cisco_role_reference.md` — expanded Webex scope and honest title variants
- `001-beast-ai-resume` clarifications — date corrections, moderate AI tone, tagline rules
- Google Drive MCP (`createFolder`, `uploadFile`, `listFolder`, `authGetStatus`)

**Storage**:
- Local staging: `artifacts/002-tailored-job-applications/`
- Google Drive folder: `Alex Rivera - SF Bay Area Applications 2026`
- Design artifacts: `specs/002-tailored-job-applications/`

**Testing**: Manual validation per [quickstart.md](./quickstart.md) — pilot role, manifest checks, keyword/traceability audits, Drive upload verification, partial re-run

**Target Platform**: Cursor agent workflow on macOS; deliverables in user's Google Drive

**Project Type**: Document transformation + MCP-integrated batch delivery (no application server)

**Performance Goals**: Full batch (40 PDFs) completable in one working session; single-role pilot ≤15 minutes; Joe locates any packet in &lt;1 minute (SC-007)

**Constraints**:
- Honesty-first (FR-004, SC-004); no fabrication
- ATS-friendly markdown (FR-009): single column, no tables/images
- PDF final deliverables only in Drive (FR-006)
- Qualys ends March 2022; Webex March 2022 – Present (FR-010)
- Moderate AI/LLM language per 001-beast-ai-resume (FR-013)

**Scale/Scope**: 20 roles × 2 documents = 40 PDFs + manifest + batch summary

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Constitution ratified | **N/A** | `.specify/memory/constitution.md` is uninitialized template |
| Simplicity | **PASS** | Markdown + manifest + MCP uploads; no custom application server |
| Testability | **PASS** | quickstart.md defines 11 verifiable scenarios including pilot-first gate |
| Honesty / traceability | **PASS** | data-model V-001; resume contract C-13/C-14; research R2 category templates |
| User-requested integrations | **PASS** | Drive MCP and PDF delivery captured as business requirements |

**Post-design re-check**: PASS — design artifacts contain no unjustified complexity.

## Project Structure

### Documentation (this feature)

```text
specs/002-tailored-job-applications/
├── plan.md              # This file
├── research.md          # Phase 0 — role inventory, tailoring, PDF, Drive pipeline
├── data-model.md        # Phase 1 — entities, validation, state transitions
├── quickstart.md        # Phase 1 — validation guide
├── contracts/
│   ├── job-opportunity-manifest-schema.md
│   ├── resume-markdown-schema.md
│   ├── cover-letter-schema.md
│   └── file-naming-convention.md
└── tasks.md             # Phase 2 (/speckit-tasks — not yet created)
```

### Runtime Artifacts (created during implementation)

```text
JOBHUNT/
├── sf_bay_area_job_opportunities.md     # Source (unchanged)
├── joe_zanini_resume.md                 # Source (unchanged)
├── cisco_role_reference.md              # Supplemental source
└── artifacts/002-tailored-job-applications/
    ├── batch/
    │   ├── manifest.json                # 20-role state tracker
    │   └── summary.md                   # Human-readable completion report
    ├── resumes/
    │   └── {role_id}.md                 # ×20
    ├── cover-letters/
    │   └── {role_id}.md                 # ×20
    └── pdf/
        └── {role_id}_{type}.pdf         # Local staging before upload
```

**Structure Decision**: Document + batch-artifact feature. No `src/` or `tests/` directories. Agent authors content against contracts; manifest enables FR-012 partial re-runs. Drive is system of record for final PDFs.

## Phase 0: Research — Complete

See [research.md](./research.md). All NEEDS CLARIFICATION items resolved:

- 20-role canonical inventory with `role_id` slugs
- Per-category tailoring templates
- PDF pipeline: Pandoc / npx md-to-pdf with Google Doc export fallback
- Drive MCP tool mapping (`createFolder`, `uploadFile`)
- File naming convention and collision handling
- Warning flags for stretch, citizenship, thin-data roles

## Phase 1: Design — Complete

| Artifact | Path | Purpose |
|----------|------|---------|
| Data model | [data-model.md](./data-model.md) | Entities, relationships, validation rules |
| Manifest contract | [contracts/job-opportunity-manifest-schema.md](./contracts/job-opportunity-manifest-schema.md) | 20-role JSON schema |
| Resume contract | [contracts/resume-markdown-schema.md](./contracts/resume-markdown-schema.md) | Per-role ATS resume structure |
| Cover letter contract | [contracts/cover-letter-schema.md](./contracts/cover-letter-schema.md) | Per-role cover letter structure |
| Naming contract | [contracts/file-naming-convention.md](./contracts/file-naming-convention.md) | Drive PDF file names |
| Quickstart | [quickstart.md](./quickstart.md) | Pilot-first validation scenarios |

**Agent context**: Updated manually in `.cursor/rules/specify-rules.mdc` (script skipped — PyYAML unavailable).

## Phase 2: Implementation Outline (for `/speckit-tasks`)

1. **Initialize batch infrastructure** — Create `artifacts/002-tailored-job-applications/` tree; populate `manifest.json` with all 20 roles from research R1; verify Drive auth; create Drive folder.
2. **Pilot single role** — Generate resume + cover letter for `fractional-ai-devrel`; convert to PDF; upload; run quickstart scenarios 3–7.
3. **Generate priority-tier resumes** — Top 9 roles from Recommended Application Priority table in source file (Fractional AI, Anthropic ×3, OpenAI DX, Diagrid, Neo4j, Plaid).
4. **Generate remaining resumes** — Roles 10–20 including borderline and stretch entries with manifest warnings.
5. **Generate all cover letters** — One per role per cover-letter contract; unique body per role_id.
6. **Batch PDF conversion** — Convert all markdown to PDF; validate page counts (SC-006).
7. **Batch Drive upload** — Upload 40 PDFs with naming contract; update manifest statuses.
8. **Produce batch summary** — Write `batch/summary.md` with per-role status, file names, warnings (FR-011).
9. **Joe review pass** — Spot-check 5 roles for traceability (SC-004) and keyword coverage (SC-005); verify LinkedIn URL in contact line before submission.

## Complexity Tracking

No constitution violations. No complexity justification required.
