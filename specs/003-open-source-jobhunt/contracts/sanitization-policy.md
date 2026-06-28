# Contract: Sanitization Policy

**Feature**: `003-open-source-jobhunt` | **Version**: 1.0

Defines what MUST NOT and what MAY enter the public publish staging tree.

## Denylist (never copy)

These paths or patterns MUST NOT appear in `export/ai-jobhunt-kit/`:

| Pattern | Reason |
|---------|--------|
| `joe_zanini_resume.md` | Personal resume (PII) |
| `sf_bay_area_job_opportunities.md` | Live job search list |
| `cisco_role_reference.md` | Author-specific employer reference |
| `google_scopes.md` | OAuth scope audit (account-specific) |
| `local-paths.json` | Maintainer path mapping |
| `client_secret_*.json` | OAuth credentials |
| `.env`, `.env.*` | Secrets |
| `artifacts/002-tailored-job-applications/resumes/**` | Tailored application content |
| `artifacts/002-tailored-job-applications/cover-letters/**` | Tailored application content |
| `artifacts/002-tailored-job-applications/pdf/**` | Generated PDFs |
| `artifacts/002-tailored-job-applications/batch/contact.json` | Personal contact |
| `artifacts/002-tailored-job-applications/batch/manifest.json` | Real batch state + Drive IDs |
| `artifacts/002-tailored-job-applications/batch/summary.md` | Personal batch report |
| `export/**` | Staging itself (no recursion) |

## Content scan patterns (fail build if matched in staging)

| Pattern | Description |
|---------|-------------|
| `alex.rivera@example.com` | Maintainer email |
| `Alex Rivera` / `ALEX RIVERA` | Maintainer name |
| `\(510\) XXX-XXXX` | Maintainer phone |
| `example-alex-rivera` | LinkedIn slug |
| `REDACTED_OAUTH_CLIENT_ID` | OAuth client ID fragment |
| `Alex Rivera - SF Bay Area Applications` | Personal Drive folder name |

## Required transforms before staging

| Target | Transform |
|--------|-----------|
| `scripts/batch/convert_to_pdf.py` | Replace hard-coded phone regex with configurable read from `contact.json` or generic `PHONE_RE` from examples |
| `.cursor/rules/pdf-clickable-links.mdc` | Replace maintainer email/phone examples with fictional `alex.rivera@example.com` |
| `.cursor/rules/public-facing-grammar.mdc` | Remove author-specific references |
| `specs/**/spec.md`, `plan.md`, `quickstart.md` | Replace "Alex Rivera" with "Alex Rivera" or generic "the candidate" in examples |
| `specs/**/research.md` | Omit or redact R1 20-role inventory tied to real search; link to `examples/` instead |

## Allowlist

Only paths listed in [publish-bundle-manifest.md](./publish-bundle-manifest.md) may be copied. Copy operations outside the allowlist MUST fail the build script.

## Maintainer workspace invariant

The build script MUST:
- Use read-only access to source files
- NEVER delete, move, or modify denylist source files in `JOBHUNT/`
- Write only to `export/ai-jobhunt-kit/`

## Verification

Pre-push checklist item: run `scripts/build-publish-bundle.sh --scan-only` (or equivalent) and confirm exit code 0.
