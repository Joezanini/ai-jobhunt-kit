# Never Commit These Files

The public `ai-jobhunt-kit` repository must never contain personal job-hunt data or credentials.

## Gitignored paths (maintainer workspace)

| Path | Why |
|------|-----|
| `joe_zanini_resume.md` | Personal resume (PII) |
| `sf_bay_area_job_opportunities.md` | Live job search list |
| `cisco_role_reference.md` | Personal current-role reference |
| `local-paths.json` | Points to personal file locations |
| `artifacts/` | Tailored resumes, cover letters, PDFs, manifests |
| `export/` | Publish staging (regenerated) |
| `client_secret_*.json` | Google OAuth credentials |
| `.env`, `.env.*` | API tokens and secrets |
| `google_scopes.md` | Account-specific OAuth audit |

## Before any `git add`

```bash
git status
git check-ignore -v joe_zanini_resume.md local-paths.json
```

## Forking adopters

If you fork `ai-jobhunt-kit` for your own search:

- Keep real resume and `job_opportunities.md` **local only**
- Use `local-paths.json` (gitignored) for personal paths
- Never open a PR that includes your PII

## Publish safety

Maintainers use `scripts/build-publish-bundle.sh` (allowlist export)—not `git push` of the full private workspace.

See [PUBLISH_CHECKLIST.md](./PUBLISH_CHECKLIST.md).
