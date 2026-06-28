# Implementation Plan: Beast AI Enablement Lead Tailored Resume

**Branch**: `001-beast-ai-resume` | **Date**: 2026-06-25 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-beast-ai-resume/spec.md`

## Summary

Produce two markdown deliverables at the repository root: a tailored resume (`joe_zanini_resume_beast_ai_enablement.md`) optimized for the Beast Industries AI Enablement Lead posting, and a companion AI work examples document (`ai_work_examples_beast.md`). The approach reframes Joe's Webex developer relations and Qualys technical account management experience as embedded, builder-first enablement—using moderate AI/LLM language tied to verifiable automation, ML, and tooling work—while passing ATS keyword filters without fabrication.

## Technical Context

**Language/Version**: Markdown (GitHub-flavored); PDF via Pandoc or VS Code Markdown PDF

**Primary Dependencies**: Source resume (`joe_zanini_resume.md`), job posting (`AI_Enablement_Lead.md`), clarify-session decisions in spec

**Storage**: Plain markdown files at project root; design artifacts under `specs/001-beast-ai-resume/`

**Testing**: Manual validation per [quickstart.md](./quickstart.md) — schema conformance, keyword coverage, traceability, PDF render

**Target Platform**: Job application submission (ATS + human reviewer); local PDF generation on macOS

**Project Type**: Document transformation / job-search deliverable (no application code)

**Performance Goals**: Resume scannable in ≤30 seconds; 1–2 page PDF; ≥12/15 posting keywords present naturally

**Constraints**: Honesty-first (SC-005); no relocation on resume; moderate AI language; descriptive tagline only (no fabricated title); Qualys ends March 2022

**Scale/Scope**: 2 output files, ~1–2 pages resume + ~1 page examples annex

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Constitution ratified | **N/A** | `.specify/memory/constitution.md` is uninitialized template |
| Simplicity | **PASS** | Two markdown files; no code, no over-engineering |
| Testability | **PASS** | quickstart.md defines 7 verifiable scenarios |
| Honesty / traceability | **PASS** | research.md keyword mapping and data-model validation rules enforce SC-005 |

**Post-design re-check**: PASS — design artifacts contain no unjustified complexity.

## Project Structure

### Documentation (this feature)

```text
specs/001-beast-ai-resume/
├── plan.md              # This file
├── research.md          # Phase 0 — role mapping, ATS strategy, format decisions
├── data-model.md        # Phase 1 — resume and annex entity schema
├── quickstart.md        # Phase 1 — validation guide
├── contracts/
│   ├── resume-markdown-schema.md
│   └── ai-work-examples-schema.md
└── tasks.md             # Phase 2 (/speckit-tasks — not yet created)
```

### Deliverables (repository root)

```text
JOBHUNT/
├── joe_zanini_resume.md                      # Source (unchanged)
├── joe_zanini_resume_beast_ai_enablement.md  # Primary output
├── ai_work_examples_beast.md                 # Companion output
├── AI_Enablement_Lead.md                     # Target posting
└── specs/001-beast-ai-resume/                # Design artifacts
```

**Structure Decision**: Document-only feature. No `src/` or `tests/` directories. Implementation is content authoring against contracts in `specs/001-beast-ai-resume/contracts/`.

## Phase 0: Research — Complete

See [research.md](./research.md). All NEEDS CLARIFICATION items resolved via clarify session (dates, tagline, AI tone, examples, relocation).

## Phase 1: Design — Complete

| Artifact | Path | Purpose |
|----------|------|---------|
| Data model | [data-model.md](./data-model.md) | Entity schema and validation rules |
| Resume contract | [contracts/resume-markdown-schema.md](./contracts/resume-markdown-schema.md) | Required markdown structure |
| Examples contract | [contracts/ai-work-examples-schema.md](./contracts/ai-work-examples-schema.md) | Companion doc structure |
| Quickstart | [quickstart.md](./quickstart.md) | End-to-end validation scenarios |

**Agent context**: Updated manually in `.cursor/rules/specify-rules.mdc` (script skipped — PyYAML unavailable).

## Phase 2: Implementation Outline (for `/speckit-tasks`)

1. **Draft tailored resume** — Follow resume contract; rewrite summary, tagline, experience bullets per research keyword mapping.
2. **Draft AI work examples annex** — Webex SDK/content + Spec Kit/agentic tooling with verifiable references.
3. **Run quickstart validation** — Keyword count, date check, traceability, PDF render.
4. **Joe review pass** — Confirm Webex blog/talk URLs and LinkedIn link before submission.

## Complexity Tracking

No constitution violations. No complexity justification required.
