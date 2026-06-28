# Maintainer Local Workflow

Dual-track layout: your **private workspace** keeps working; the **public repo** is a separate sanitized export.

## What stays local (never published)

| File | Purpose |
|------|---------|
| `joe_zanini_resume.md` | Your base resume |
| `cisco_role_reference.md` | Your current-role deep reference |
| `sf_bay_area_job_opportunities.md` | Your live job list |
| `local-paths.json` | Maps agents to the files above |
| `artifacts/002-tailored-job-applications/` | Tailored apps, PDFs, manifest |
| `client_secret_*.json` | OAuth credentials |

**Invariant (FR-015)**: `build-publish-bundle.sh` never deletes, moves, or modifies these files.

## Daily job-hunt commands

1. Agents read `local-paths.json` for paths.
2. Generate tailored markdown under `artifacts/002-tailored-job-applications/`.
3. Convert PDFs locally or upload via Drive MCP.
4. Your files remain at the same paths before and after open-source publish.

## Verify paths resolve

```bash
cd /Users/joezanini/JOBHUNT
python3 -c "
import json, os
p = json.load(open('local-paths.json'))
for k, v in p.items():
    if k.startswith('$'): continue
    if k == 'candidate_name': continue
    if k == 'drive_folder_name': continue
    assert os.path.exists(v), f'Missing: {k} -> {v}'
print('All local-paths resolve OK')
"
```

## Publishing open source

```bash
./scripts/build-publish-bundle.sh          # writes export/ai-jobhunt-kit/
./scripts/build-publish-bundle.sh --scan-only
# GitHub MCP: create_repository + push_files (never push full JOBHUNT repo)
```

## After publish

Re-run one personal role pilot—no path rewiring needed if `local-paths.json` is unchanged.

See [END_TO_END_WORKFLOW.md](./END_TO_END_WORKFLOW.md).
