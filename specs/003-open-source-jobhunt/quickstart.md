# Quickstart: Validate Open-Source Publish and Local Continuity

**Feature**: `003-open-source-jobhunt`

## Prerequisites

- Private `JOBHUNT` workspace with existing personal files intact
- GitHub MCP authenticated (`get_me` returns username)
- Bash available for publish script (implementation phase)
- Design contracts in [contracts/](./contracts/)

## Setup (one-time, implementation phase)

```bash
cd /Users/joezanini/JOBHUNT

# Create maintainer local path config (gitignored)
cp local-paths.example.json local-paths.json
# Edit paths to match your real files — see contracts/local-paths-schema.md

# Verify personal files still exist
test -f joe_zanini_resume.md
test -f sf_bay_area_job_opportunities.md
test -f artifacts/002-tailored-job-applications/batch/contact.json
```

## Validation Scenarios

### 1. Personal files untouched (FR-015, SC-009)

Record checksums or timestamps before publish:

```bash
shasum -a 256 joe_zanini_resume.md sf_bay_area_job_opportunities.md
```

Run publish bundle build. Re-run `shasum`.

**Expected**: Identical hashes; files still at original paths.

### 2. Local paths resolve (FR-016)

```bash
test -f "$(python3 -c "import json; print(json.load(open('local-paths.json'))['base_resume'])")"
```

**Expected**: All required keys in `local-paths.json` point to existing files.

### 3. Gitignore blocks PII (FR-008)

```bash
git check-ignore -v joe_zanini_resume.md local-paths.json artifacts/ export/
```

**Expected**: Each path reported as ignored (after `.gitignore` update in implement phase).

### 4. Build publish staging (allowlist)

```bash
./scripts/build-publish-bundle.sh
```

**Expected**: Creates `export/ai-jobhunt-kit/`; exits 0; prints file count ≥ 40.

### 5. Staging scan — zero PII (SC-002)

```bash
./scripts/build-publish-bundle.sh --scan-only
# Or manual spot-check:
rg -i "jozanini|Alex Rivera|XXX-XXXX|REDACTED_OAUTH_CLIENT_ID" export/ai-jobhunt-kit/ && exit 1 || echo "PASS"
```

**Expected**: No matches for maintainer PII patterns.

### 6. Denylist files absent from staging

```bash
test ! -f export/ai-jobhunt-kit/joe_zanini_resume.md
test ! -d export/ai-jobhunt-kit/artifacts/002-tailored-job-applications/resumes
test ! -f export/ai-jobhunt-kit/local-paths.json
```

**Expected**: All tests pass.

### 7. Examples present for adopters (SC-005)

```bash
test -f export/ai-jobhunt-kit/examples/sample_resume.md
test -f export/ai-jobhunt-kit/examples/sample_job_opportunities.md
test -f export/ai-jobhunt-kit/local-paths.example.json
```

**Expected**: Fictional persona only (Alex Rivera); no maintainer email.

### 8. README completeness (SC-004, SC-007)

Inspect `export/ai-jobhunt-kit/README.md` against [readme-outline.md](./contracts/readme-outline.md).

**Expected**: Sections 1–13 present; subsections for Cursor, Claude Code, and Codex under §8.

### 9. Pre-publish checklist (SC-001)

Complete `docs/PUBLISH_CHECKLIST.md` against staging tree.

**Expected**: 100% items checked before GitHub push.

### 10. Create public GitHub repository (FR-001)

GitHub MCP `create_repository`:
- `name`: `ai-jobhunt-kit`
- `private`: `false`
- `description`: per SC-008
- `autoInit`: `false` (push from staging)

**Expected**: Repository URL returned; visibility public.

### 11. Push staging to GitHub (FR-017)

GitHub MCP `push_files` from `export/ai-jobhunt-kit/` contents.

**Expected**: Initial commit on `main`; only allowlisted files.

### 12. Secret scan (FR-003)

GitHub MCP `run_secret_scanning` on new repo (if available).

**Expected**: No verified secrets.

### 13. Maintainer continuity pilot (SC-009)

Using **unchanged** `local-paths.json` and personal files:

1. Pick one real role from `sf_bay_area_job_opportunities.md`
2. Regenerate or verify existing tailored markdown under `artifacts/002-tailored-job-applications/`
3. Convert one resume to PDF locally

**Expected**: Success without editing paths post-publish.

### 14. Adopter fresh-clone pilot (SC-003)

In a **separate** directory:

```bash
git clone https://github.com/<owner>/ai-jobhunt-kit.git /tmp/ai-jobhunt-kit-test
cd /tmp/ai-jobhunt-kit-test
cp local-paths.example.json local-paths.json
mkdir -p artifacts/pilot/{resumes,cover-letters,pdf,batch}
```

Follow README §6 to generate pilot resume + cover letter for one example role.

**Expected**: Two markdown files + two PDFs in under 90 minutes without maintainer assistance.

## Failure recovery

| Failure | Action |
|---------|--------|
| Staging scan finds PII | Fix transform rules; rebuild; do not push |
| Personal file missing after build | **STOP** — build script violated FR-015; fix script |
| `local-paths.json` tracked by git | Add to `.gitignore`; `git rm --cached` if staged |
| Secret scan alerts | Rotate credential; remove from history; rebuild staging |

## Links

- [Sanitization policy](./contracts/sanitization-policy.md)
- [Local paths schema](./contracts/local-paths-schema.md)
- [Publish bundle manifest](./contracts/publish-bundle-manifest.md)
- [README outline](./contracts/readme-outline.md)
- [Data model](./data-model.md)
