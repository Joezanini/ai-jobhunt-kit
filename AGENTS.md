# Agent Instructions — AI Job Hunt Kit

For OpenAI Codex and other agentic CLIs using this repository.

## Primary directive

Follow [docs/END_TO_END_WORKFLOW.md](docs/END_TO_END_WORKFLOW.md) using paths from `local-paths.json`.

## Required inputs

| File | Key in local-paths.json |
|------|-------------------------|
| Base resume | `base_resume` |
| Current role reference | `current_role_reference` |
| Job list (output of discovery) | `job_opportunities` |
| Contact JSON | `contact` |

Templates: `examples/sample_*.md` and `examples/sample_contact.json`.

## Style rules

When writing resumes or cover letters:

- [docs/CURSOR_RULES.md](docs/CURSOR_RULES.md)
- [docs/GRAMMAR_STYLE.md](docs/GRAMMAR_STYLE.md)
- `specs/002-tailored-job-applications/contracts/resume-markdown-schema.md`

## LinkedIn MCP (optional)

1. Read starter files for keywords.
2. `search_jobs` with location and date filters.
3. `get_job_details` per job_id.
4. Write `job_opportunities.md` matching `examples/sample_job_opportunities.md`.

See [docs/LINKEDIN_JOB_DISCOVERY.md](docs/LINKEDIN_JOB_DISCOVERY.md).

## Google Drive MCP (optional)

After PDF generation, `createFolder` + `uploadFile`. See [docs/DRIVE_UPLOAD.md](docs/DRIVE_UPLOAD.md).

## PDF conversion

```bash
python3 scripts/batch/convert_to_pdf.py --paths local-paths.json
```

## Security

Never commit personal resume, job list, or OAuth credentials. See [docs/NEVER_COMMIT.md](docs/NEVER_COMMIT.md).
