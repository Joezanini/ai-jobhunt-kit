# Contract: Cover Letter Markdown Schema

**Version**: 1.0.0 | **Feature**: `002-tailored-job-applications`

## Purpose

Defines per-role cover letter at:

`artifacts/002-tailored-job-applications/cover-letters/{role_id}.md`

## Document Structure (ordered)

```markdown
Alex Rivera
alex.rivera@example.com · (555) 010-0200 · LinkedIn
[Month Day, Year]

Hiring Manager
[Company]
[Role Title]

Dear Hiring Manager,

[Paragraph 1: 2–4 sentences — express interest in this specific role and company; cite one posting-aligned theme]

[Paragraph 2: 3–5 sentences — Webex DevRel / partner engineering achievement with concrete outcome]

[Paragraph 3: 3–5 sentences — Qualys TAM or AI tooling / SDK work relevant to role; optional honest nod to growth area for stretch roles]

[Paragraph 4: 2–3 sentences — closing enthusiasm, availability, thank you]

Sincerely,
Alex Rivera
```

## Constraints

| Rule | ID | Description |
|------|-----|-------------|
| Company name appears in header block | CL-01 | |
| Role title appears in header block | CL-02 | |
| First person throughout | CL-03 | |
| No fabricated metrics or employers | CL-04 | |
| No salary negotiation unless posting invites | CL-05 | |
| Does not duplicate resume bullets verbatim | CL-06 | |
| `citizenship_required` roles: optional eligibility sentence or manifest warning only | CL-07 | |
| `recruiting_firm` roles: address Kinora Group; do not invent end client | CL-08 | |
| Renders to ≤1 page PDF | CL-09 | |
| Unique body text per role_id | CL-10 | |

## Stretch Role Guidance (CL-11)

For `technical_stretch` roles (IBM, AMD, NVIDIA): acknowledge transferable DevRel strengths in paragraphs 2–3; do not claim deep domain expertise (Presto/Spark/GPU training) not supported by source materials.
