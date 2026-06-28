# Cursor Project Rules

This toolkit ships three Cursor rules in `.cursor/rules/`. They guide agent behavior during resume generation, cover letters, and PDF export.

## Rules overview

| File | `alwaysApply` | Purpose |
|------|---------------|---------|
| `specify-rules.mdc` | **true** | Points agents to the current Spec Kit plan (`specs/002-tailored-job-applications/plan.md` in development; generic plan in public export) |
| `public-facing-grammar.mdc` | false (globs) | Grammar, tense, and tone for resumes and cover letters |
| `pdf-clickable-links.mdc` | false (globs) | Ensures PDF output has clickable email, phone, and URL links |

## specify-rules.mdc

- Loaded on **every** agent turn (`alwaysApply: true`).
- Tells the agent where to read tech stack, structure, and shell commands.
- After cloning the public repo, this points to the bundled plan under `specs/`.

## public-facing-grammar.mdc

- Applies when editing files matching `**/resumes/**/*.md`, `**/cover-letters/**/*.md`, or your `base_resume` path.
- Enforces: parallel bullet verbs, present tense for current role, Oxford commas, cover letter sign-off format.
- Adopters: replicate as a Claude Code project instruction or Codex `AGENTS.md` section.

## pdf-clickable-links.mdc

- Applies when editing resume/cover letter markdown or `convert_to_pdf.py`.
- Rules: plain-text email/phone in source; `[LinkedIn](url)` for labeled links; verify PDF output has no raw `](mailto:` artifacts.
- Canonical implementation: `scripts/batch/convert_to_pdf.py`.

## Replicating outside Cursor

### Claude Code

Add to `CLAUDE.md`:

```markdown
When writing resumes or cover letters, follow docs/CURSOR_RULES.md and docs/GRAMMAR_STYLE.md.
When converting to PDF, follow pdf-clickable-links rules in docs/CURSOR_RULES.md.
```

### OpenAI Codex / agentic CLI

Mirror the same instructions in `AGENTS.md` at repo root.

## Public export note

Published `ai-jobhunt-kit` copies depersonalized rules—no maintainer email, phone, or name in examples.
