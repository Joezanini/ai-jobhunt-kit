# LinkedIn Job Discovery (MCP)

Build `job_opportunities.md` from live LinkedIn postings using the LinkedIn MCP server.

**Prerequisites**: [STARTER_FILES.md](./STARTER_FILES.md) complete; [MCP_SETUP.md](./MCP_SETUP.md) LinkedIn section done.

## Step 1: Verify authentication

```
Tool: get_my_profile (user-mcp-server-linkedin)
```

Confirm your profile returns successfully.

## Step 2: Derive search keywords

Read your two starter files:

- `local-paths.json` → `base_resume` (skills, recent titles)
- `local-paths.json` → `current_role_reference` (domain emphasis)

Example keyword sets:

- `"developer relations engineer"`
- `"AI enablement" OR "developer advocate"`
- `"technical evangelist" platform`

## Step 3: Search jobs

```
Tool: search_jobs
Arguments:
  keywords: "developer relations engineer"
  location: "San Francisco Bay Area"   # or "Remote"
  date_posted: "past_week"             # optional
  work_type: "remote,hybrid"           # optional
  max_pages: 3
```

Save returned `job_id` values.

## Step 4: Fetch details

For each `job_id`:

```
Tool: get_job_details
Arguments:
  job_id: "<id from search_jobs>"
```

Extract: company, title, location, description, URL.

## Step 5: Compile `job_opportunities.md`

Structure each role like `examples/sample_job_opportunities.md`:

```markdown
## 1. Company Name — Role Title

**Location**: ...  
**Work model**: ...  
**LinkedIn**: https://...

### Job summary
...

### Why this fits
...
```

Add a **Quick Links** section at the end with LinkedIn URLs.

## Step 6: Update manifest (batch mode)

Initialize or extend `artifacts_root/batch/manifest.json` per `specs/002-tailored-job-applications/contracts/job-opportunity-manifest-schema.md`.

## Manual fallback (no LinkedIn MCP)

1. Save interesting postings from linkedin.com/jobs.
2. Paste summaries into `job_opportunities.md` using the template above.
3. Continue with Spec Kit tailoring—MCP is optional (FR-014).

## Agent prompt (Cursor / Claude / Codex)

```text
Read local-paths.json. Using LinkedIn MCP search_jobs and get_job_details,
search for [YOUR KEYWORDS] in [LOCATION]. Write results to the job_opportunities
path as markdown matching examples/sample_job_opportunities.md. Include fit notes
based on base_resume and current_role_reference. Do not fabricate qualifications.
```

## Next step

[END_TO_END_WORKFLOW.md](./END_TO_END_WORKFLOW.md) step 5 — tailored resume and cover letter generation.
