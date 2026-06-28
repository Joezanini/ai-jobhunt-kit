# Contract: Tailored Resume Markdown Schema

**Version**: 1.0.0 | **Feature**: `001-beast-ai-resume`

## Purpose

Defines the required structure for `joe_zanini_resume_beast_ai_enablement.md` so implementers and validators share a single format contract.

## Document Structure (ordered)

```markdown
# ALEX RIVERA

Technical Enablement · Workflow Automation · Developer Advocacy

alex.rivera@example.com · LinkedIn · (555) 010-0200 · San Francisco Bay Area, CA

## Summary

[3–5 sentences]

## Experience

### [Job Title]
**[Company]** · [Start] – [End]

- [Bullet]
- [Bullet]

[Repeat per role]

## Education

### [Degree]
**[Institution]** · [Graduation]

## Skills

**AI & Automation:** [comma-separated list]

**Engineering:** [comma-separated list]

**Enablement:** [comma-separated list]
```

## Constraints

| Rule | ID |
|------|-----|
| Exactly one H1 (`#`) — candidate name | C-01 |
| Tagline is plain text on line immediately after H1; not a `##` heading | C-02 |
| Contact on single line after tagline | C-03 |
| Section headers use `##` only | C-04 |
| Job titles use `###`; company/dates on next line in bold company format | C-05 |
| Bullets use `-` only (not `●`) | C-06 |
| No tables, images, or HTML | C-07 |
| No relocation language in header | C-08 |
| Target 1–2 pages PDF at standard margins | C-09 |
| Skills use bold group labels with colon separator | C-10 |

## Prohibited Content

- Fabricated job titles in tagline or summary
- "Present" on more than one full-time concurrent role
- Keyword stuffing (same phrase >3 times outside Skills)
- Disqualifying lead phrases: "curriculum design," "L&D program," "training program owner"

## Acceptance

Document conforms when all C-01 through C-10 pass and FR-001 through FR-013 from spec.md are satisfied.
