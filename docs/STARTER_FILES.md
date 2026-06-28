# Starter Files: Resume + Current Role Reference

Before running LinkedIn job discovery or generating tailored applications, prepare **two local files**. Both paths are configured in `local-paths.json` (copy from `local-paths.example.json`).

## File A: Base resume (`base_resume`)

**Purpose**: Canonical facts for every tailored resume—contact, employment history, education, skills.

**Maintainer example**: `joe_zanini_resume.md` (gitignored)  
**Adopter example**: `examples/sample_resume.md`

### Required sections

- Name and contact line (email, LinkedIn, phone, location)
- Summary or bio (3–5 sentences)
- Experience (employer, title, dates, bullets)
- Education
- Skills (grouped if helpful)

### Rules

- Every bullet must be traceable to real experience (no fabricated employers or dates).
- Use ATS-friendly markdown: single column, no tables or images.
- See `specs/002-tailored-job-applications/contracts/resume-markdown-schema.md`.

## File B: Current role reference (`current_role_reference`)

**Purpose**: Deep context on your **current** role that does not fit on a one-page resume—title variants, project list, partner scope, OSS stewardship, conference talks, honest framing for stretch roles.

**Maintainer example**: `cisco_role_reference.md` (gitignored)  
**Adopter example**: `examples/sample_role_reference.md`

### Recommended sections

| Section | Content |
|---------|---------|
| How the role is labeled | Official title vs. self-described vs. resume title |
| Role summary | 1–2 paragraphs on scope |
| Key responsibilities | Bullets by theme (evangelism, OSS, partner work, etc.) |
| Projects and content | Links to blogs, SDKs, samples |
| Honest title guidance | When to use which title on tailored resumes |

### Rules

- Supplement the resume; do not contradict dates or employers.
- Agents use this file when tailoring emphasis and choosing bullets.
- Never commit your real file to a public fork—keep it gitignored.

## Configure `local-paths.json`

```json
{
  "$schema": "local-paths-v1",
  "base_resume": "path/to/your_resume.md",
  "current_role_reference": "path/to/your_role_reference.md",
  "job_opportunities": "path/to/job_opportunities.md",
  "contact": "path/to/contact.json",
  "artifacts_root": "artifacts/pilot/",
  "candidate_name": { "first": "Your", "last": "Name" }
}
```

## Next step

Continue to [END_TO_END_WORKFLOW.md](./END_TO_END_WORKFLOW.md) step 2 (Cursor rules and MCP setup).
