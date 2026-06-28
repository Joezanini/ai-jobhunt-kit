# Requirements Traceability

Maps functional requirements (FR) to README and doc artifacts in the public `ai-jobhunt-kit` repository.

| FR | Requirement summary | Artifact |
|----|---------------------|----------|
| FR-001 | Public GitHub repo via MCP | `scripts/build-publish-bundle.sh` + publish tasks; repo created at implement time |
| FR-002 | No author PII in public repo | `docs/NEVER_COMMIT.md`, `scripts/build-publish-bundle.sh` scan |
| FR-003 | No credentials | `.gitignore`, `docs/NEVER_COMMIT.md`, scan patterns |
| FR-004 | No real application artifacts | Denylist in build script |
| FR-005 | Reusable workflow assets | `.specify/`, `.cursor/`, `specs/`, `scripts/batch/` |
| FR-006 | Root README sections | `README.md` |
| FR-007 | Placeholder templates | `examples/` |
| FR-008 | Expanded gitignore | `.gitignore` (staging copy) |
| FR-009 | Pre-publish checklist | `docs/PUBLISH_CHECKLIST.md` |
| FR-010 | LICENSE | `LICENSE` |
| FR-011 | Honesty standards | README § Honesty; `specs/001-beast-ai-resume/` |
| FR-012 | Identity via local-paths | `local-paths.example.json`, `docs/STARTER_FILES.md` |
| FR-013 | Architecture docs | `docs/END_TO_END_WORKFLOW.md` |
| FR-014 | MCP optional | README § Minimal path |
| FR-015 | Maintainer files stay local | `docs/MAINTAINER_LOCAL_WORKFLOW.md`, build script FR-015 comment |
| FR-016 | Gitignored local-paths | `local-paths.example.json` vs gitignored `local-paths.json` |
| FR-017 | Separate public export | `scripts/build-publish-bundle.sh` → `export/ai-jobhunt-kit/` |

## Success criteria mapping

| SC | README / doc anchor |
|----|---------------------|
| SC-003 | Quick start + END_TO_END_WORKFLOW |
| SC-004 | README § Tool-specific setup; CLAUDE.md; AGENTS.md |
| SC-005 | `examples/sample_resume.md`, `examples/sample_job_opportunities.md` |
| SC-007 | README table of contents |
| SC-008 | GitHub repo description at create time |
