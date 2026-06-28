# Contract: Tailored Resume Markdown Schema

**Version**: 1.0.0 | **Feature**: `002-tailored-job-applications`  
**Extends**: `001-beast-ai-resume/contracts/resume-markdown-schema.md`

## Purpose

Defines per-role resume structure at:

`artifacts/002-tailored-job-applications/resumes/{role_id}.md`

## Document Structure (ordered)

```markdown
# ALEX RIVERA

[Role-aligned tagline — descriptive phrases, not a job title]

alex.rivera@example.com · LinkedIn · (555) 010-0200 · San Francisco Bay Area, CA

## Summary

[3–5 sentences tailored to role category and keyword_targets]

## Experience

### Webex Developer Relations Engineer
**Webex** · March 2022 – Present

- [Role-reframed bullet]
- [Role-reframed bullet]

### Team Lead, Technical Account Manager — Post Sales SMB
**Qualys** · June 2020 – March 2022

- [Role-reframed bullet]

[Additional roles as in source — Bonfire, Dor]

## Education

### B.A. Computer Science
**The University of California, Santa Cruz** · June 2020

## Skills

**[Category-appropriate group 1]:** [comma-separated]

**[Category-appropriate group 2]:** [comma-separated]

**[Category-appropriate group 3]:** [comma-separated]
```

## Skill Group Templates by Category

| Category | Suggested groups |
|----------|------------------|
| `devrel` | Developer Relations, Engineering & APIs, Community & Content |
| `ai_enablement` | AI & Developer Tools, Engineering, Enablement & Workshops |
| `partner_gtm` | Partner Engineering, Cloud & Integrations, Customer Engagement |
| `engineering` | Platform Engineering, APIs & SDKs, Languages & Tools |
| `stretch` | Developer Advocacy, Engineering Foundations, [Domain-adjacent honest skills] |
| `support_alt` | Technical Support & Automation, Engineering, Customer Success |

## Constraints

Inherits C-01 through C-10 from `001-beast-ai-resume` resume contract, plus:

| Rule | ID |
|------|-----|
| Tagline MUST differ across roles (not identical copy-paste) | C-11 |
| Summary MUST reference role category emphasis | C-12 |
| ≥5 `keyword_targets` from manifest appear naturally in body | C-13 |
| Webex bullets MAY use expanded scope from `cisco_role_reference.md` | C-14 |
| No relocation language in header | C-15 |
| Resume MUST fit 1–2 pages when rendered to PDF | C-16 |

## Traceability

Each bullet MUST map to a source in `joe_zanini_resume.md` or `cisco_role_reference.md`. Document mapping in implementer notes if non-obvious.
