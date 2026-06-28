# MCP Setup: LinkedIn and Google Drive

Optional MCP servers extend the job-hunt workflow. Core value (markdown + local PDF) works without them—see README minimal path.

## LinkedIn MCP (`user-mcp-server-linkedin`)

### Purpose

Discover jobs on LinkedIn and fetch posting details for `job_opportunities.md`.

### Key tools

| Tool | Use |
|------|-----|
| `get_my_profile` | Verify authenticated session |
| `search_jobs` | Search by keywords, location, filters; returns `job_id` list |
| `get_job_details` | Full description for each `job_id` |

### Setup (Cursor)

1. Open **Cursor Settings → MCP**.
2. Add the LinkedIn MCP server per your server's README (typically requires LinkedIn session/cookies).
3. Restart Cursor; confirm tools appear in the MCP panel.

### Auth troubleshooting

- If `search_jobs` returns empty or errors, re-authenticate per server docs.
- Use [LINKEDIN_JOB_DISCOVERY.md](./LINKEDIN_JOB_DISCOVERY.md) manual fallback: paste postings into `job_opportunities.md`.

## Google Drive MCP (`user-drive`)

### Purpose

Upload PDF resumes and cover letters to a dedicated Drive folder.

### Key tools

| Tool | Use |
|------|-----|
| `authGetStatus` | Verify OAuth connection and scopes |
| `authListScopes` | Diagnose missing Drive permissions |
| `createFolder` | Batch folder for this job search |
| `uploadFile` | Upload local PDF (`localPath`, `name`, `parentFolderId`) |
| `listFolder` | Verify uploads |

### Setup (Cursor)

1. Create a Google Cloud OAuth client (Desktop or Web) with Drive API enabled.
2. Configure the Drive MCP server with your client credentials (**never commit** `client_secret_*.json`).
3. Run `authGetStatus` after first connect.

### Scope notes

- Prefer narrow scopes (`drive.file`) when possible.
- See your server's documentation for required scopes.

## GitHub MCP (maintainers only)

Used to create and push the public `ai-jobhunt-kit` repository—not required for day-to-day job applications.

Tools: `create_repository`, `push_files`, `run_secret_scanning`.

## Claude Code / Codex

MCP availability varies by product. If MCP is unavailable:

- **LinkedIn**: Build `job_opportunities.md` manually from saved postings.
- **Drive**: Use local PDFs only or upload via drive.google.com manually.

## Next steps

- [LINKEDIN_JOB_DISCOVERY.md](./LINKEDIN_JOB_DISCOVERY.md)
- [DRIVE_UPLOAD.md](./DRIVE_UPLOAD.md)
- [END_TO_END_WORKFLOW.md](./END_TO_END_WORKFLOW.md)
