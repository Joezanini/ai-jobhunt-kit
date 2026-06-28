# Publish Checklist

Complete every item before pushing `export/ai-jobhunt-kit/` to the public GitHub repository.

## CHK-001: Personal files untouched

- [ ] `shasum -a 256 joe_zanini_resume.md cisco_role_reference.md` unchanged after bundle build

## CHK-002: Local paths resolve

- [ ] All keys in `local-paths.json` point to existing files (maintainer workflow)

## CHK-003: Gitignore coverage

- [ ] `git check-ignore -v joe_zanini_resume.md local-paths.json artifacts/ export/` reports ignored

## CHK-004: Staging build succeeds

- [ ] `./scripts/build-publish-bundle.sh` exits 0
- [ ] Staging file count ≥ 40

## CHK-005: PII scan passes

- [ ] `./scripts/build-publish-bundle.sh --scan-only` exits 0
- [ ] Manual: `rg -i "jozanini|Alex Rivera|XXX-XXXX|REDACTED_OAUTH_CLIENT_ID" export/ai-jobhunt-kit/` returns no matches

## CHK-006: Denylist absent from staging

- [ ] No `joe_zanini_resume.md` in staging
- [ ] No `artifacts/002-tailored-job-applications/resumes/` in staging
- [ ] No `local-paths.json` in staging (only `local-paths.example.json`)

## CHK-007: Examples use fictional persona

- [ ] `examples/sample_contact.json` contains Alex Rivera only
- [ ] No maintainer LinkedIn slug in tracked files

## CHK-008: README complete

- [ ] README has starter files, Cursor rules, LinkedIn MCP, Drive MCP, Cursor/Claude/Codex sections
- [ ] Links to `docs/END_TO_END_WORKFLOW.md`

## CHK-009: LICENSE present

- [ ] `export/ai-jobhunt-kit/LICENSE` exists (MIT)

## Pre-push verification

```bash
./scripts/build-publish-bundle.sh
./scripts/build-publish-bundle.sh --scan-only
rg -i "jozanini|Alex Rivera|XXX-XXXX" export/ai-jobhunt-kit/ && exit 1 || echo "PII scan PASS"
```

**Sign-off**: _________________ **Date**: _________

Only proceed to GitHub `push_files` when all boxes are checked.
