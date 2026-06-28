# Contract: README Outline

**Feature**: `003-open-source-jobhunt` | **Version**: 1.0

Required sections for the public repository root `README.md`. Order is normative (FR-006, SC-007).

## 1. Title and description

- Project name: **AI Job Hunt Kit** (or `ai-jobhunt-kit`)
- One paragraph: agent-driven toolkit for tailored resumes, cover letters, and batch PDF delivery using Spec Kit workflows
- Who it is for: developers using AI coding assistants for job applications

## 2. Table of contents

Anchor links to all major sections below.

## 3. What this repo includes / does not include

| Included | Not included |
|----------|--------------|
| Spec Kit specs and contracts | Your personal resume or job list |
| Example fictional data | Live job scraping |
| Batch scripts and PDF guidance | Hosted service or SaaS |
| Multi-tool setup instructions | Pre-filled application PDFs |

## 4. Prerequisites

- Git
- AI coding assistant (pick one path in §8)
- PDF tool: Pandoc **or** `npx md-to-pdf`
- Optional: Google Drive MCP, GitHub MCP, LinkedIn MCP

## 5. Repository layout

```text
ai-jobhunt-kit/
├── examples/           # Copy and customize locally
├── specs/              # Feature specs and contracts
├── scripts/batch/      # PDF conversion
├── .cursor/            # Cursor skills and rules
├── .specify/           # Spec Kit configuration
└── local-paths.example.json
```

## 6. Quick start (adopter — 30 minutes)

1. Clone repository
2. Copy `local-paths.example.json` → `local-paths.json`
3. Copy `examples/*` to personal paths **or** point `local-paths.json` at `examples/` for dry run
4. Create `artifacts/pilot/{resumes,cover-letters,pdf,batch}/`
5. Run single-role pilot per `specs/002-tailored-job-applications/quickstart.md` (sanitized paths)

## 7. Maintainer vs adopter workflows

- **Adopters**: Start from `examples/`; never commit real PII
- **Maintainers forking for themselves**: Use `local-paths.json` (gitignored) for real files; see `docs/PUBLISH_CHECKLIST.md` before any public push

## 8. Tool-specific setup

### 8a. Cursor (with Spec Kit)

- Open folder in Cursor
- Skills auto-load from `.cursor/skills/`
- Run `/speckit-specify`, `/speckit-plan`, `/speckit-implement` workflow
- Optional MCP: configure Drive/GitHub in Cursor settings

### 8b. Claude Code

- Clone repo; add `CLAUDE.md` summarizing §6 and pointing to `specs/002-tailored-job-applications/quickstart.md`
- Copy relevant skill instructions from `.cursor/skills/speckit-implement/SKILL.md` into project context
- Use same file layout and `local-paths.json`

### 8c. OpenAI Codex / agentic CLI

- Clone repo; ensure `AGENTS.md` or repo instructions mirror §6
- Invoke agent with prompt: "Follow specs/002-tailored-job-applications/quickstart.md pilot scenario using local-paths.json"
- PDF conversion via `scripts/batch/convert_to_pdf.py` or pandoc commands in `scripts/batch/README.md`

## 9. Honesty and traceability

- Link to resume contract C-13/C-14 concepts
- No fabricated employers, titles, or dates
- Moderate AI language standard from `001-beast-ai-resume`

## 10. Full batch workflow

- Manifest schema reference
- 20-role scale optional; pilot uses 2 example roles
- Partial re-run (FR-012 pattern)
- Optional Drive upload section

## 11. Configuring personal data locally

- Document `local-paths.json` fields
- List gitignored paths users should create
- Warning: do not commit resume, contact.json, or artifacts with real applications

## 12. Contributing and license

- MIT License
- Link to `docs/PUBLISH_CHECKLIST.md` for contributors
- How to report issues on GitHub

## 13. Acknowledgments

- Spec Kit, prior feature specs
- Optional maintainer GitHub username (no email/phone)

## Acceptance

README is complete when SC-004, SC-006, SC-007, and SC-008 are verifiable by section inspection.
