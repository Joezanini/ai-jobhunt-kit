# End-to-End Workflow

From zero to submission-ready application PDFs using AI coding assistants, Spec Kit, and optional MCP servers.

## Overview

```text
Starter files → Cursor rules + MCP → LinkedIn job list → Tailored markdown → PDF → Drive upload
```

| Step | Action | Doc |
|------|--------|-----|
| 1 | Prepare base resume + current role reference | [STARTER_FILES.md](./STARTER_FILES.md) |
| 2 | Enable Cursor rules and Spec Kit skills | [CURSOR_RULES.md](./CURSOR_RULES.md) |
| 3 | Configure LinkedIn + Drive MCP (optional) | [MCP_SETUP.md](./MCP_SETUP.md) |
| 4 | Build job_opportunities.md via LinkedIn MCP | [LINKEDIN_JOB_DISCOVERY.md](./LINKEDIN_JOB_DISCOVERY.md) |
| 5 | Generate tailored resume + cover letter per role | Spec Kit + `specs/002-tailored-job-applications/` |
| 6 | Convert markdown to PDF | `scripts/batch/convert_to_pdf.py` |
| 7 | Upload PDFs to Google Drive | [DRIVE_UPLOAD.md](./DRIVE_UPLOAD.md) |
| 8 | (Maintainers) Publish open-source toolkit | `scripts/build-publish-bundle.sh` |

---

## Step 1: Two starter files

Create and configure paths in `local-paths.json`:

1. **`base_resume`** — Up-to-date resume markdown.
2. **`current_role_reference`** — Detailed current-role description.

Copy `local-paths.example.json` → `local-paths.json` and customize.

**Cursor rules that apply**: None yet (source material only).

---

## Step 2: Cursor rules and Spec Kit

Open the project in **Cursor**. These rules load automatically:

| Rule | When it applies |
|------|-----------------|
| `specify-rules.mdc` | Every agent turn — reads current plan for structure and commands |
| `public-facing-grammar.mdc` | Editing resumes and cover letters |
| `pdf-clickable-links.mdc` | Resume/cover letter markdown and PDF conversion |

Run Spec Kit commands as needed:

- `/speckit-specify` — define a batch or tailoring feature
- `/speckit-plan` — design contracts and quickstart
- `/speckit-implement` — execute tasks

Skills live in `.cursor/skills/speckit-*/`.

**Claude Code / Codex**: Use `CLAUDE.md` and `AGENTS.md` at repo root.

---

## Step 3: MCP setup (optional)

- **LinkedIn MCP**: `search_jobs`, `get_job_details` — see [MCP_SETUP.md](./MCP_SETUP.md).
- **Google Drive MCP**: `authGetStatus`, `createFolder`, `uploadFile`.

Skip this step for markdown-only pilot; add MCP when ready for discovery and cloud delivery.

---

## Step 4: LinkedIn job discovery

Agent workflow:

1. Read `base_resume` and `current_role_reference`.
2. Call `search_jobs` with derived keywords and location filters.
3. Call `get_job_details` for each result.
4. Write `job_opportunities.md` matching `examples/sample_job_opportunities.md`.

See [LINKEDIN_JOB_DISCOVERY.md](./LINKEDIN_JOB_DISCOVERY.md).

**Cursor rules**: `specify-rules.mdc` (plan context if running a Spec Kit feature for batch).

---

## Step 5: Tailored applications

For each role in `job_opportunities.md`:

1. Read contracts in `specs/002-tailored-job-applications/contracts/`.
2. Generate `artifacts_root/resumes/{role_id}.md` and `cover-letters/{role_id}.md`.
3. Trace every bullet to `base_resume` or `current_role_reference` — no fabrication.

**Cursor rules**:

- `public-facing-grammar.mdc` — tone, tense, bullets, cover letter sign-off
- `specify-rules.mdc` — implementation plan and honesty constraints

---

## Step 6: PDF conversion

```bash
# From repo root; requires pandoc or use convert_to_pdf.py
python3 scripts/batch/convert_to_pdf.py --paths local-paths.json
```

Or see `scripts/batch/README.md` for pandoc one-liners.

**Cursor rules**: `pdf-clickable-links.mdc` — verify clickable email, phone, LinkedIn in output PDF.

---

## Step 7: Google Drive upload

1. `authGetStatus` → `createFolder` → `uploadFile` per PDF.
2. Update `batch/manifest.json`.

See [DRIVE_UPLOAD.md](./DRIVE_UPLOAD.md).

---

## Step 8: Open-source publish (maintainers only)

```bash
./scripts/build-publish-bundle.sh
./scripts/build-publish-bundle.sh --scan-only
# Then GitHub MCP: create_repository + push_files
```

Personal files (`joe_zanini_resume.md`, etc.) stay local—never moved. See [MAINTAINER_LOCAL_WORKFLOW.md](./MAINTAINER_LOCAL_WORKFLOW.md).

---

## Minimal path (no MCP)

1. Starter files (step 1)
2. Cursor rules (step 2)
3. Manually author `job_opportunities.md`
4. Tailor markdown (step 5)
5. Local PDF (step 6)

This satisfies core toolkit value without LinkedIn or Drive integrations.
