# AI Job Hunt Kit

Agent-driven toolkit for tailored resumes, cover letters, and batch PDF delivery using [Spec Kit](https://github.com/github/spec-kit) workflows. Built for developers using AI coding assistants (Cursor, Claude Code, Codex) who want honest, ATS-friendly application materials without a hosted SaaS.

## Table of contents

- [What this includes](#what-this-includes)
- [Two starter files (required)](#two-starter-files-required)
- [Prerequisites](#prerequisites)
- [Repository layout](#repository-layout)
- [Quick start](#quick-start)
- [End-to-end workflow](#end-to-end-workflow)
- [Cursor project rules](#cursor-project-rules)
- [LinkedIn MCP — job discovery](#linkedin-mcp--job-discovery)
- [Google Drive MCP — PDF upload](#google-drive-mcp--pdf-upload)
- [Minimal path (no MCP)](#minimal-path-no-mcp)
- [Tool-specific setup](#tool-specific-setup)
- [Honesty and traceability](#honesty-and-traceability)
- [Full batch workflow](#full-batch-workflow)
- [Personal data (keep local)](#personal-data-keep-local)
- [Contributing and license](#contributing-and-license)

## What this includes

| Included | Not included |
|----------|--------------|
| Spec Kit specs, contracts, and skills | Your personal resume or job list |
| Fictional example data in `examples/` | Live job scraping service |
| Batch PDF scripts and grammar rules | Pre-filled application PDFs for you |
| [LinkedIn](https://github.com/stickerdaniel/linkedin-mcp-server) + [Drive]() MCP documentation | Required MCP (optional enhancements) |

## Two starter files (required)

Before any job search or LinkedIn discovery, create:

1. **`base_resume`** — Up-to-date resume markdown ([template](examples/sample_resume.md))
2. **`current_role_reference`** — Detailed current-role description ([template](examples/sample_role_reference.md))

Configure paths in `local-paths.json` (copy from `local-paths.example.json`). See [docs/STARTER_FILES.md](docs/STARTER_FILES.md).

## Prerequisites

- Git
- AI coding assistant (see [Tool-specific setup](#tool-specific-setup))
- PDF: `pip install markdown xhtml2pdf` **or** `brew install pandoc`
- **Optional**: [LinkedIn MCP](docs/MCP_SETUP.md#linkedin-mcp-user-mcp-server-linkedin), [Google Drive MCP](docs/MCP_SETUP.md#google-drive-mcp-user-drive)

## Repository layout

```text
ai-jobhunt-kit/
├── examples/              # Fictional starter files
├── docs/                  # End-to-end guides
├── specs/                 # Feature specs and contracts
├── scripts/batch/         # PDF conversion
├── .cursor/
│   ├── skills/speckit-*   # Spec Kit agent skills
│   └── rules/*.mdc        # Cursor project rules
├── .specify/              # Spec Kit configuration
├── local-paths.example.json
├── CLAUDE.md              # Claude Code entry point
└── AGENTS.md              # Codex / agentic CLI entry point
```

## Quick start

1. `git clone https://github.com/<owner>/ai-jobhunt-kit.git && cd ai-jobhunt-kit`
2. `cp local-paths.example.json local-paths.json`
3. For dry run, keep paths pointing at `examples/`; for real search, replace with your local gitignored files
4. `mkdir -p artifacts/pilot/{resumes,cover-letters,pdf,batch}`
5. Copy `examples/sample_manifest.json` → `artifacts/pilot/batch/manifest.json`
6. Follow [docs/END_TO_END_WORKFLOW.md](docs/END_TO_END_WORKFLOW.md)

## End-to-end workflow

| Step | Action |
|------|--------|
| 1 | [Starter files](docs/STARTER_FILES.md) |
| 2 | [Cursor rules](docs/CURSOR_RULES.md) + Spec Kit skills |
| 3 | [MCP setup](docs/MCP_SETUP.md) (optional) |
| 4 | [LinkedIn job list](docs/LINKEDIN_JOB_DISCOVERY.md) |
| 5 | Tailored resume + cover letter per `specs/002-tailored-job-applications/` |
| 6 | `python3 scripts/batch/convert_to_pdf.py --paths local-paths.json` |
| 7 | [Drive upload](docs/DRIVE_UPLOAD.md) (optional) |

Full guide: **[docs/END_TO_END_WORKFLOW.md](docs/END_TO_END_WORKFLOW.md)**

## Cursor project rules

Three rules in `.cursor/rules/` shape agent output:

| Rule | Purpose |
|------|---------|
| `specify-rules.mdc` | Spec Kit plan context (always on) |
| `public-facing-grammar.mdc` | Resume/cover letter tone and grammar |
| `pdf-clickable-links.mdc` | Clickable email, phone, URLs in PDFs |

Details: [docs/CURSOR_RULES.md](docs/CURSOR_RULES.md)

## LinkedIn MCP — job discovery

Use `search_jobs` and `get_job_details` to build `job_opportunities.md` from your resume and role reference keywords.

**Guide**: [docs/LINKEDIN_JOB_DISCOVERY.md](docs/LINKEDIN_JOB_DISCOVERY.md)  
**Setup**: [docs/MCP_SETUP.md](docs/MCP_SETUP.md)

## Google Drive MCP — PDF upload

Use `authGetStatus`, `createFolder`, and `uploadFile` to store submission-ready PDFs.

**Guide**: [docs/DRIVE_UPLOAD.md](docs/DRIVE_UPLOAD.md)

## Minimal path (no MCP)

Markdown generation and local PDF work **without** LinkedIn or Drive MCP:

1. Starter files → 2. Cursor rules → 3. Manual `job_opportunities.md` → 4. Tailor → 5. PDF

MCP sections above are optional enhancements (FR-014).

## Tool-specific setup

### Cursor (with Spec Kit)

- Open folder in Cursor; skills load from `.cursor/skills/`
- Rules load from `.cursor/rules/` (see [CURSOR_RULES.md](docs/CURSOR_RULES.md))
- Commands: `/speckit-specify`, `/speckit-plan`, `/speckit-implement`
- Configure LinkedIn and Drive MCP in Cursor Settings → MCP

### Claude Code

- Read [CLAUDE.md](CLAUDE.md) at repo root
- Mirror Cursor rules in project instructions
- Same file layout and `local-paths.json`

### OpenAI Codex / agentic CLI

- Read [AGENTS.md](AGENTS.md)
- Prompt: *"Follow docs/END_TO_END_WORKFLOW.md using local-paths.json"*

## Honesty and traceability

- No fabricated employers, titles, dates, or accomplishments
- Every tailored bullet must trace to `base_resume` or `current_role_reference`
- Moderate AI language standard: see `specs/001-beast-ai-resume/`
- Contracts: `specs/002-tailored-job-applications/contracts/resume-markdown-schema.md`

## Full batch workflow

- Manifest schema: `specs/002-tailored-job-applications/contracts/job-opportunity-manifest-schema.md`
- Pilot: 2 example roles in `examples/sample_manifest.json`
- Scale: add roles to manifest and `job_opportunities.md`
- Partial re-run: set one role `status` to `pending` and regenerate
- Optional Drive upload per [DRIVE_UPLOAD.md](docs/DRIVE_UPLOAD.md)

## Personal data (keep local)

**Never commit**: real resume, role reference, job list, `contact.json` with your info, `artifacts/` with applications, OAuth secrets.

See [docs/NEVER_COMMIT.md](docs/NEVER_COMMIT.md). Use `local-paths.json` (gitignored) for personal paths.

## Contributing and license

MIT License — see [LICENSE](LICENSE).

Maintainers: [docs/PUBLISH_CHECKLIST.md](docs/PUBLISH_CHECKLIST.md) before any public push.

Report issues on GitHub.

## Acknowledgments

Built with [Spec Kit](https://github.com/github/spec-kit). Example persona and companies are fictional.
