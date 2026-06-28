# Quickstart: Validate Tailored Resume Deliverables

**Feature**: `001-beast-ai-resume`

## Prerequisites

- Markdown resume and companion files implemented at project root:
  - `joe_zanini_resume_beast_ai_enablement.md`
  - `ai_work_examples_beast.md`
- Optional: `pandoc` for PDF validation (`brew install pandoc`)

## Validation Scenarios

### 1. Schema conformance

```bash
cd /Users/joezanini/JOBHUNT
test -f joe_zanini_resume_beast_ai_enablement.md
test -f ai_work_examples_beast.md
```

**Expected**: Both files exist.

Review against [resume-markdown-schema.md](./contracts/resume-markdown-schema.md) and [ai-work-examples-schema.md](./contracts/ai-work-examples-schema.md).

### 2. Employment date consistency (SC-001)

Open resume and confirm:

| Role | Dates |
|------|-------|
| Webex | March 2022 – Present |
| Qualys | June 2020 – March 2022 |
| Bonfire | March 2021 – August 2021 |
| Dor Technologies | July 2019 – March 2020 |

**Expected**: Only Webex shows "Present."

### 3. Keyword coverage (SC-002)

Search resume (case-insensitive) for posting terms. Target ≥12 hits among:

`AI`, `embed` or `partner`, `automation`, `workflow`, `tool`, `LLM` or `agent`, `prompt`, `evaluation`, `deploy` or `ship`, `non-technical`, `self-directed` or `resourceful`, `productivity` or `impact`, `cross-functional`, `experiment`

```bash
rg -i 'ai|embed|partner|automation|workflow|tool|llm|agent|prompt|evaluat|deploy|ship|non-technical|self-directed|resourceful|productivity|impact|cross-functional|experiment' joe_zanini_resume_beast_ai_enablement.md
```

**Expected**: Natural occurrences in context; not isolated keyword lists.

### 4. Traceability check (SC-005)

For each experience bullet, confirm mapping to `joe_zanini_resume.md` or spec clarifications.

**Expected**: Zero fabricated employers, titles, or products.

### 5. PDF render (SC-004)

```bash
pandoc joe_zanini_resume_beast_ai_enablement.md -o /tmp/joe_resume_beast.pdf
open /tmp/joe_resume_beast.pdf
```

**Expected**: 1–2 pages; headers, tagline, contact, bullets intact.

### 6. AI work examples (SC-006)

Open `ai_work_examples_beast.md` and verify:

1. Webex Python SDK / content example has a working public URL
2. Spec Kit / agentic tooling example references this repository

**Expected**: Both links/paths resolve; descriptions match actual work.

### 7. 30-second recruiter scan (SC-003)

Ask a reviewer (or self-review after 24h) to read only the name, tagline, and summary.

**Expected**: Primary fit identified as embedded technical enablement / dev rel; not "trainer" or "generic engineer."

## Pass Criteria

All seven scenarios pass → ready to submit with Beast application.

## References

- [spec.md](./spec.md) — requirements and success criteria
- [data-model.md](./data-model.md) — entity definitions
- [research.md](./research.md) — keyword and reframing decisions
