# Data Model: Open-Source AI Job Hunting Toolkit

**Feature**: `003-open-source-jobhunt` | **Date**: 2026-06-27

This feature manages a dual-track file layout: private maintainer workspace vs public publish bundle. No database.

## Entity: LocalPathConfiguration

Gitignored file (`local-paths.json`) mapping logical workflow keys to filesystem paths. Maintainer instance points to real PII files; adopters copy from `local-paths.example.json`.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `base_resume` | string (path) | yes | Must exist on disk for maintainer runs |
| `job_opportunities` | string (path) | yes | Markdown file |
| `role_reference` | string (path) | no | Supplemental facts markdown |
| `contact` | string (path) | yes | JSON per contact shape below |
| `artifacts_root` | string (path) | yes | Directory; contains batch/, resumes/, etc. |
| `candidate_name` | object | yes | `first`, `last` for file naming |
| `drive_folder_name` | string | no | Optional; maintainer-only cloud label |

**Rules**:
- File MUST be listed in `.gitignore` (FR-016)
- `local-paths.example.json` uses `examples/` paths and fictional name "Alex Rivera"
- Agents resolve logical keys through this config before reading sources

## Entity: ContactConfiguration

JSON contact block used by PDF conversion and resume header lines.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `name` | string | yes | Display name |
| `email` | string | yes | Valid email format |
| `phone` | string | no | Display format |
| `phone_tel` | string | no | E.164 for `tel:` links |
| `linkedin` | string (URL) | no | |
| `location` | string | no | |
| `resume_contact_line` | string | yes | Markdown one-liner for resume |
| `cover_letter_contact_line` | string | yes | Markdown for cover letter |

**Public example**: `examples/sample_contact.json` only.  
**Private instance**: `artifacts/.../batch/contact.json` — never exported.

## Entity: SanitizationPolicy

Rules governing publish staging. See [sanitization-policy.md](./contracts/sanitization-policy.md).

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `denylist_globs` | string[] | yes | Non-empty |
| `allowlist_globs` | string[] | yes | Non-empty; disjoint from denylist targets |
| `transforms` | TransformRule[] | yes | Applied during staging build |
| `scan_patterns` | string[] | yes | Regex for emails, phones, client_secret |

### TransformRule

| Field | Type | Description |
|-------|------|-------------|
| `target_glob` | string | File pattern in staging |
| `action` | enum | `depersonalize_regex`, `replace_string`, `exclude` |
| `params` | object | Action-specific |

## Entity: PublishStagingTree

Ephemeral directory `export/ai-jobhunt-kit/` produced by build script.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `root_path` | string | yes | `export/ai-jobhunt-kit/` |
| `file_count` | integer | yes | Matches bundle manifest |
| `build_timestamp` | ISO datetime | yes | |
| `scan_status` | enum | yes | `pending`, `passed`, `failed` |
| `scan_findings` | string[] | no | Populated on failure |

**State transitions**:

```text
[empty] → build_started → copy_allowlist → apply_transforms → scan
  scan → passed → ready_for_github_push
  scan → failed → (fix sources, rebuild)
  ready_for_github_push → pushed → archived (staging may be deleted)
```

## Entity: PublicRepository

GitHub repository created for open source.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `name` | string | yes | e.g. `ai-jobhunt-kit` |
| `owner` | string | yes | GitHub username or org |
| `visibility` | enum | yes | `public` |
| `description` | string | yes | Per SC-008 |
| `default_branch` | string | yes | `main` |
| `license` | string | yes | `MIT` |
| `initial_commit_sha` | string | no | Set after `push_files` |

## Entity: PublishChecklist

Human-executable gate before GitHub push.

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `items` | ChecklistItem[] | yes | All must pass |
| `completed_at` | ISO datetime | no | Set when all checked |
| `signoff` | string | no | Maintainer initials |

### ChecklistItem

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | e.g. `CHK-001` |
| `description` | string | Verifiable statement |
| `passed` | boolean | |

**Minimum items**: staging scan clean; no denylist files in tree; examples use fictional persona; LICENSE present; README has 3 tool sections; maintainer personal files untouched; `local-paths.json` still gitignored.

## Entity: TemplateBundle

Sanitized files shipped in public repo under `examples/`.

| Asset | Path | Purpose |
|-------|------|---------|
| Sample resume | `examples/sample_resume.md` | Adopter pilot base facts |
| Sample opportunities | `examples/sample_job_opportunities.md` | 2 fictional roles |
| Sample role reference | `examples/sample_role_reference.md` | Supplemental facts pattern |
| Sample contact | `examples/sample_contact.json` | Fictional contact |
| Sample manifest | `examples/sample_manifest.json` | 2-role batch state |

## Entity: PrivateWorkspaceInventory

Maintainer files that MUST remain local and MUST NOT appear in PublicRepository.

| Category | Paths |
|----------|-------|
| Identity sources | `joe_zanini_resume.md` |
| Live job search | `sf_bay_area_job_opportunities.md` |
| Employer-specific reference | `cisco_role_reference.md` |
| Credentials | `client_secret_*.json`, `.env*` |
| OAuth debug | `google_scopes.md` |
| Generated applications | `artifacts/002-tailored-job-applications/**` (except depersonalized scripts copied to staging) |
| Local config | `local-paths.json` |
| Staging | `export/` |

**Invariant** (FR-015): Publish workflow MUST NOT delete, move, or overwrite any PrivateWorkspaceInventory path.

## Relationships

```text
LocalPathConfiguration ──reads──► PrivateWorkspaceInventory (maintainer)
LocalPathConfiguration ──reads──► TemplateBundle (adopter)

SanitizationPolicy ──governs──► PublishStagingTree
PublishBundleManifest ──defines──► PublishStagingTree contents

PublishStagingTree ──push_files──► PublicRepository
PublishChecklist ──gates──► PublicRepository creation

TemplateBundle ──included_in──► PublishStagingTree
```

## Validation Rules Summary

| ID | Rule |
|----|------|
| V-001 | Staging tree MUST NOT contain any PrivateWorkspaceInventory file content |
| V-002 | Staging scan MUST fail on maintainer email `alex.rivera@example.com` or phone `(555) 010-0200` |
| V-003 | `local-paths.json` MUST NOT be tracked in public repo |
| V-004 | After publish, maintainer `local-paths.json` paths MUST still resolve to existing files |
| V-005 | Public repo MUST contain ≥1 sample role in `examples/sample_job_opportunities.md` |
