# Implementation Plan: Open-Source AI Job Hunting Toolkit

**Branch**: `003-open-source-jobhunt` | **Date**: 2026-06-27 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/003-open-source-jobhunt/spec.md`

## Summary

Package the Spec Kit–driven job-hunting workflow into a **separate public GitHub repository** created via the GitHub MCP integration. The maintainer's private `JOBHUNT` workspace keeps all personal files (`joe_zanini_resume.md`, `sf_bay_area_job_opportunities.md`, tailored artifacts, credentials) in place and gitignored; a allowlist-based **publish staging** tree (`export/ai-jobhunt-kit/`) receives only sanitized toolkit assets. A root README documents reproduction for Cursor, Claude Code, and Codex. Local continuity is enforced via gitignored `local-paths.json` and expanded `.gitignore` rules—not by relocating or deleting personal data.

## Technical Context

**Language/Version**: Markdown, JSON, YAML (Spec Kit); Bash publish script; Python 3 (optional PDF conversion depersonalization)

**Primary Dependencies**:
- Spec Kit `.specify/` configuration, skills, and workflows from this workspace
- Sanitized copies of `001-beast-ai-resume` and `002-tailored-job-applications` specs/contracts
- GitHub MCP (`create_repository`, `push_files`, `run_secret_scanning`)
- Optional: Google Drive / LinkedIn MCP (documented as optional for adopters)
- Prior feature contracts: resume, cover letter, manifest, file-naming schemas (depersonalized)

**Storage**:
- **Local private workspace** (`JOBHUNT/`): unchanged personal paths; gitignored PII
- **Publish staging** (`export/ai-jobhunt-kit/`): regenerable; never committed to private workspace remote if contaminated
- **Public GitHub repo** (new): `ai-jobhunt-kit` or similar—system of record for open source
- **Examples** (`examples/` in public repo): fictional sample resume, job list, contact, manifest

**Testing**: Manual validation per [quickstart.md](./quickstart.md)—publish checklist, staging scan, maintainer continuity pilot, fresh-clone adopter pilot

**Target Platform**: macOS maintainer workspace; public repo tool-agnostic (Cursor, Claude Code, Codex)

**Project Type**: Documentation + agent-workflow toolkit export (no application server)

**Performance Goals**: Publish staging build ≤5 minutes; adopter pilot ≤90 minutes (SC-003); maintainer post-publish re-run ≤15 minutes (SC-009)

**Constraints**:
- Zero PII/credentials in public repo (FR-002–FR-004, SC-002)
- Maintainer files stay in place (FR-015)
- Allowlist export only—never `git push` entire private repo (FR-017)
- Depersonalize `convert_to_pdf.py` phone regex and cursor rules before export
- Clean git history for public repo initial commit (no leaked secrets from local history)

**Scale/Scope**: ~50–80 allowlisted files in public repo; 15+ gitignore patterns; 3 tool-specific README sections; 4 contracts

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Constitution ratified | **N/A** | `.specify/memory/constitution.md` is uninitialized template |
| Simplicity | **PASS** | Allowlist copy + gitignore + separate public repo; no monorepo split tooling |
| Testability | **PASS** | quickstart.md defines maintainer continuity + adopter clone scenarios |
| Privacy / security | **PASS** | sanitization-policy contract; pre-publish checklist; secret scan step |
| User-requested continuity | **PASS** | local-paths schema; FR-015/016; no file moves |

**Post-design re-check**: PASS — dual-track design adds only `local-paths.json` and publish script; no unjustified complexity.

## Project Structure

### Documentation (this feature)

```text
specs/003-open-source-jobhunt/
├── plan.md              # This file
├── research.md          # Phase 0 — dual-track, export, GitHub, tool paths
├── data-model.md        # Phase 1 — publish entities, local paths, staging state
├── quickstart.md        # Phase 1 — validation guide
├── contracts/
│   ├── sanitization-policy.md
│   ├── local-paths-schema.md
│   ├── publish-bundle-manifest.md
│   └── readme-outline.md
└── tasks.md             # Phase 2 (/speckit-tasks — not yet created)
```

### Runtime Layout (after implementation)

```text
JOBHUNT/                              # Private working workspace (stays local)
├── joe_zanini_resume.md              # GITIGNORED — maintainer keeps using
├── sf_bay_area_job_opportunities.md  # GITIGNORED
├── cisco_role_reference.md           # GITIGNORED (author-specific)
├── client_secret_*.json              # GITIGNORED
├── local-paths.json                  # GITIGNORED — points agents to personal files
├── local-paths.example.json          # TRACKED — template for adopters
├── artifacts/002-tailored-job-applications/  # GITIGNORED (entire tree)
├── export/ai-jobhunt-kit/            # GITIGNORED staging (regenerated)
├── scripts/
│   └── build-publish-bundle.sh       # Allowlist copy + depersonalize
└── specs/ ...                        # Specs sanitized on export, full locally

export/ai-jobhunt-kit/                # Staging → pushed to public GitHub
├── README.md
├── LICENSE
├── examples/
│   ├── sample_resume.md
│   ├── sample_job_opportunities.md
│   ├── sample_role_reference.md
│   └── sample_contact.json
├── .specify/                         # Sanitized Spec Kit config
├── .cursor/                          # Depersonalized rules + skills
├── specs/                            # 001/002/003 sanitized
├── scripts/batch/                    # convert_to_pdf.py (generic phone regex)
└── docs/PUBLISH_CHECKLIST.md
```

**Structure Decision**: Dual-track—private workspace is the maintainer's live environment; public repo is a curated export. Personal files are never moved; `.gitignore` + `local-paths.json` preserve continuity. Adopters clone public repo only and copy `examples/` to their own gitignored paths.

## Phase 0: Research — Complete

See [research.md](./research.md). All Technical Context items resolved—no NEEDS CLARIFICATION remain.

## Phase 1: Design — Complete

| Artifact | Path | Purpose |
|----------|------|---------|
| Data model | [data-model.md](./data-model.md) | Local vs public entities, staging lifecycle |
| Sanitization policy | [contracts/sanitization-policy.md](./contracts/sanitization-policy.md) | Denylist, allowlist, transform rules |
| Local paths schema | [contracts/local-paths-schema.md](./contracts/local-paths-schema.md) | Gitignored maintainer config |
| Publish bundle manifest | [contracts/publish-bundle-manifest.md](./contracts/publish-bundle-manifest.md) | Files included in public repo |
| README outline | [contracts/readme-outline.md](./contracts/readme-outline.md) | Required onboarding sections |
| Quickstart | [quickstart.md](./quickstart.md) | Maintainer + adopter validation |

**Agent context**: Updated in `.cursor/rules/specify-rules.mdc` → this plan.

## Phase 2: Implementation Outline (for `/speckit-tasks`)

1. **Expand `.gitignore`** — Add personal source files, `artifacts/`, `local-paths.json`, `export/`, `google_scopes.md`, and credential patterns per sanitization policy.
2. **Add `local-paths.example.json` + maintainer `local-paths.json`** — Map resume, opportunities, role reference, contact, artifacts root to current paths.
3. **Author fictional `examples/` sources** — Sample resume, job list (1–2 roles), role reference, contact for public bundle.
4. **Write `scripts/build-publish-bundle.sh`** — Allowlist copy to `export/ai-jobhunt-kit/`; depersonalize cursor rules, convert_to_pdf phone regex, spec prose; fail on denylist hits.
5. **Sanitize specs for export** — Replace author names in 001/002/003 spec examples; keep contracts generic.
6. **Write public `README.md`** per readme-outline contract (Cursor, Claude Code, Codex sections).
7. **Add `LICENSE` (MIT)** and `docs/PUBLISH_CHECKLIST.md`.
8. **Run publish checklist + staging scan** — Verify zero PII/secrets in staging tree.
9. **Create public GitHub repo** — `create_repository` (public, `ai-jobhunt-kit`).
10. **Push initial commit** — `push_files` from staging; run `run_secret_scanning` if available.
11. **Maintainer continuity test** — Re-run one personal role using unchanged local files (SC-009).
12. **Optional** — Add `private/README.md` in workspace explaining what stays local (not exported).

## Complexity Tracking

No constitution violations. Dual-track export is justified: making the whole `JOBHUNT` repo public would leak PII; deleting/moving personal files would break the active job search.
