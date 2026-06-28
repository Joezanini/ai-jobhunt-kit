# Claude Code — AI Job Hunt Kit

Use this repo with Claude Code for agent-driven job applications.

## Start here

1. [docs/STARTER_FILES.md](docs/STARTER_FILES.md) — create resume + current role reference
2. [docs/END_TO_END_WORKFLOW.md](docs/END_TO_END_WORKFLOW.md) — full pipeline
3. `local-paths.json` — copy from `local-paths.example.json`

## Workflow summary

1. Prepare **base_resume** and **current_role_reference** markdown files.
2. Apply grammar rules from [docs/CURSOR_RULES.md](docs/CURSOR_RULES.md) and [docs/GRAMMAR_STYLE.md](docs/GRAMMAR_STYLE.md).
3. **Optional**: LinkedIn MCP — [docs/LINKEDIN_JOB_DISCOVERY.md](docs/LINKEDIN_JOB_DISCOVERY.md) to build `job_opportunities.md`.
4. Generate tailored resume and cover letter per `specs/002-tailored-job-applications/contracts/`.
5. `python3 scripts/batch/convert_to_pdf.py --paths local-paths.json`
6. **Optional**: Drive MCP — [docs/DRIVE_UPLOAD.md](docs/DRIVE_UPLOAD.md)

## MCP

- LinkedIn: `search_jobs`, `get_job_details` — [docs/MCP_SETUP.md](docs/MCP_SETUP.md)
- Google Drive: `authGetStatus`, `createFolder`, `uploadFile`

## Minimal path

Skip MCP steps; write `job_opportunities.md` manually and produce local PDFs only.

## Honesty

Do not fabricate experience. Trace bullets to starter files only.
