# Feature Specification: Open-Source AI Job Hunting Toolkit

**Feature Branch**: `003-open-source-jobhunt`

**Created**: 2026-06-27

**Status**: Draft

**Input**: User description: "I want to bottle this up. Can you use the github MCP server to create a Repository that makes this jobhunting tool Open-source. Make sure that no PII or Sensitive credentials or tokens makes it to this Repository. I want the README to outline exactly what someone needs to do to reproduce this job hunting set up on their local AI tools, like Claude and Codex alike."

**Clarifications**

### Session 2026-06-27

- Q: Should the maintainer lose or relocate personal files when open-sourcing? → A: No. Local copies of PII and sensitive personal files MUST remain in the working workspace at their current paths so the maintainer can continue the job-hunt workflow unchanged; only the separate public export omits them.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Publish a Sanitized Public Repository (Priority: P1)

A maintainer packages the job-hunting workflow—Spec Kit feature specs, batch pipeline contracts, agent skills, cursor rules, and conversion scripts—into a new **public** GitHub repository created via the connected GitHub integration. The repository contains everything a stranger needs to understand and fork the workflow, with all personal data, application artifacts, and secrets removed or replaced with placeholders.

**Why this priority**: Without a clean public repository, nothing else can be shared or reproduced; leaking PII or credentials would undermine trust and safety.

**Independent Test**: Clone the new public repository to a fresh directory. Run an automated and manual secret/PII scan. Confirm zero matches for real names, emails, phone numbers, OAuth client files, API tokens, or personal job-application PDFs from the original workspace.

**Acceptance Scenarios**:

1. **Given** the maintainer has GitHub integration access, **When** the publish workflow completes, **Then** a public repository exists with a descriptive name, short description, and initial commit containing only approved open-source content.
2. **Given** the published repository, **When** a reviewer compares it to the private workspace inventory, **Then** every excluded category (personal resume, contact files, tailored application artifacts, OAuth credentials, job-opportunity lists tied to a real search) is absent and no substitute reintroduces real PII.
3. **Given** the published repository, **When** a clone is inspected, **Then** included content covers the end-to-end workflow: specification templates, batch manifest schema, resume/cover-letter contracts, PDF conversion guidance, and agent-oriented configuration—using sample/placeholder data only.

---

### User Story 2 - Reproduce the Workflow with Local AI Tools (Priority: P2)

A new user clones the public repository and follows the README to recreate the job-hunting setup on their machine using their preferred AI coding assistant (e.g., Cursor with Spec Kit, Claude Code, OpenAI Codex, or comparable agentic IDEs). They can run a documented "first role" pilot—create a base resume, add a job opportunity, generate tailored markdown, convert to PDF, and optionally upload to their own cloud storage—without needing access to the original author's data.

**Why this priority**: The README is the primary onboarding path; the repository has no value to the community if reproduction steps are incomplete or tool-specific to one product only.

**Independent Test**: A tester unfamiliar with the original workspace follows only the README (no private context). Within one working session they complete the pilot role using their chosen AI tool and produce two PDFs from sample inputs.

**Acceptance Scenarios**:

1. **Given** a fresh clone and the README prerequisites section, **When** the user completes setup, **Then** they have configured their own base resume file, job opportunities source, optional cloud-storage integration, and PDF conversion tool as documented.
2. **Given** the README agent workflow section, **When** the user invokes the documented Spec Kit commands (or equivalent skill/prompt sequence for non-Cursor tools), **Then** they can generate a tailored resume and cover letter for the sample job opportunity following the published contracts.
3. **Given** the README multi-tool section, **When** a user on Cursor, Claude Code, or Codex follows the tool-specific subsection, **Then** each path describes where to place rules/skills, how to run the batch pilot, and which MCP servers (if any) are optional vs required.
4. **Given** sample data in the repository, **When** the user runs the pilot, **Then** output file names follow the published naming convention with the user's own name substituted via documented configuration—not hard-coded author identity.

---

### User Story 3 - Enforce Privacy and Secret Hygiene (Priority: P3)

Before and after publishing, the maintainer runs validation that blocks personal identifiable information, application artifacts from a real job search, and sensitive credentials from entering version control. The repository documents what must stay local and provides ignore rules and pre-publish checklists so contributors do not accidentally commit secrets.

**Why this priority**: Open-sourcing a job-hunt workspace carries high risk of exposing contact details, employer-target lists, and OAuth material; prevention is non-negotiable.

**Independent Test**: Deliberately place representative sensitive files (fake credentials, sample contact.json, personal resume) in a staging tree and confirm the publish pipeline or documented checklist flags every item before push.

**Acceptance Scenarios**:

1. **Given** the publish checklist, **When** executed against the staging tree, **Then** it fails if any file matches excluded patterns: OAuth client secrets, environment files with tokens, personal contact manifests, real tailored resumes/cover letters, generated PDFs, or job lists documenting a specific individual's live search.
2. **Given** the repository `.gitignore` and documented "never commit" list, **When** a contributor follows them, **Then** common leak vectors (PDF output folders, `client_secret_*.json`, local contact overrides, personal opportunity markdown) are blocked by default.
3. **Given** a successful publish, **When** GitHub secret scanning (or equivalent documented scan) runs on the repository, **Then** no verified secrets are reported.

---

### User Story 4 - Maintainer Continues Local Workflow Uninterrupted (Priority: P4)

The original author keeps using their existing personal resume, job opportunity list, role reference, contact configuration, tailored artifacts, and credentials locally. Open-sourcing does not delete, move, or overwrite these files. A documented local-path configuration and expanded ignore rules ensure daily job-hunt commands still resolve to the author's real data while the public repository receives only sanitized templates.

**Why this priority**: Without continuity, open-sourcing would break the author's active job search—the opposite of the intended outcome.

**Independent Test**: After the publish workflow completes, run the existing single-role batch pilot against the author's real `joe_zanini_resume.md` and personal job list without restoring from backup. Confirm tailored markdown and PDF generation succeed using local paths only.

**Acceptance Scenarios**:

1. **Given** the publish workflow has run, **When** the maintainer opens their local workspace, **Then** all personal source files (resume, opportunities, role reference, contact config, artifacts) remain present and unchanged at their pre-publish paths.
2. **Given** a gitignored `local-paths.json` (or equivalent), **When** agents and scripts resolve input files, **Then** they read the maintainer's personal paths by default while example paths serve adopters who clone the public repo.
3. **Given** the maintainer runs a batch re-run for any personal role, **When** generation completes, **Then** output lands in the local `artifacts/` tree and optional Drive upload—not in the public GitHub repository.

---

### User Story 5 - Ship Templates and Examples Instead of Personal Artifacts (Priority: P5)

The public repository includes sanitized templates—sample base resume, sample job opportunities file, sample role reference, placeholder contact configuration, and an empty or demo manifest—so users understand data shape and honesty/traceability standards without copying the author's career history.

**Why this priority**: Templates lower the barrier to first success and encode the contracts defined in prior features without exposing private content.

**Independent Test**: Replace all sample files with user-authored content per README instructions; run the pilot batch for one role; confirm manifest and naming convention work with zero references to the original author remaining in config.

**Acceptance Scenarios**:

1. **Given** the `examples/` or equivalent template directory, **When** a user copies templates to their working paths, **Then** every required field for batch processing is documented with placeholder values and comments explaining honesty/traceability rules.
2. **Given** published specs from features `001` and `002`, **When** reviewed in the public repo, **Then** personal names, employers from the author's search, and Bay Area-specific opportunity text are generalized or replaced with fictional sample postings.
3. **Given** cursor rules and agent skills included in the repo, **When** inspected, **Then** they contain no hard-coded personal email, phone, or LinkedIn URLs.

---

### Edge Cases

- **Partial clone with leaked history**: If the source workspace already committed secrets locally, publishing must not push git history containing them; use a clean export or `git filter-repo` when history is contaminated.
- **MCP optional paths**: Users without Google Drive or LinkedIn MCP must still complete markdown generation and local PDF conversion per README "minimal path."
- **Fork with personal data**: README must warn users never to commit their real resume or applications back to a public fork without sanitizing.
- **License ambiguity**: Repository includes an explicit open-source license file; default assumption is MIT unless maintainer chooses otherwise before publish.
- **Spec Kit version drift**: README notes minimum Spec Kit version and where to find upgrade guidance if commands differ.
- **Multi-role batch scale**: README documents full-batch expectations (manifest, re-run single role, summary) referencing published contracts without requiring the author's 20-role dataset.
- **Grammar/style rules**: Public-facing grammar and PDF link rules ship as reusable agent rules with examples that use fictional contact data.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST create a new **public** GitHub repository via the connected GitHub integration, with repository name, description, and visibility set for open-source community use.
- **FR-002**: System MUST exclude from the published repository all personal identifiable information belonging to the original author, including legal name in config files, email addresses, phone numbers, physical location, personal LinkedIn/GitHub profile URLs, and employer-specific job-hunt target lists tied to a real search campaign.
- **FR-003**: System MUST exclude all sensitive credentials and tokens, including OAuth client secret JSON files, API keys, environment files containing secrets, and authenticated session material.
- **FR-004**: System MUST exclude generated application deliverables from the real job search: tailored resumes, cover letters, PDFs, batch manifests recording real role IDs with personal file names, and Google Drive folder IDs from the author's account.
- **FR-005**: System MUST include the reusable workflow assets: Spec Kit configuration (`.specify/`), feature specifications and contracts (sanitized), agent skills and cursor rules (depersonalized), batch conversion scripts, and JSON/markdown schemas for resumes, cover letters, manifests, and file naming.
- **FR-006**: System MUST provide a root README that documents, in order: project purpose; prerequisites; repository layout; step-by-step local setup; configuring personal data locally (kept out of git); running the single-role pilot; running a full batch; optional MCP integrations (Drive, GitHub, LinkedIn); and tool-specific paths for **Cursor**, **Claude Code**, and **Codex** (or equivalent agentic assistants).
- **FR-007**: System MUST ship placeholder/template data files sufficient to run the pilot workflow without the author's real resume or job list.
- **FR-008**: System MUST expand ignore rules so personal data paths, PDF outputs, OAuth patterns, and local override files cannot be committed accidentally.
- **FR-009**: System MUST include a pre-publish checklist (human-executable) listing every exclusion category and verification step; publish proceeds only when all items pass.
- **FR-010**: System MUST include an open-source LICENSE file in the repository root.
- **FR-011**: System MUST document honesty and traceability standards (no fabricated employers, titles, or accomplishments) inherited from prior features so adopters understand content quality expectations.
- **FR-012**: System MUST document how adopters substitute their own identity in contact configuration and file naming without editing multiple scattered files.
- **FR-013**: System MUST retain architectural documentation explaining the relationship between base resume, job opportunities source, tailored artifacts, manifest tracking, and optional cloud upload—at a level understandable to non-developers evaluating the toolkit.
- **FR-014**: System MUST NOT require adopters to use Google Drive or any specific MCP server to obtain core value (markdown generation and local PDF output).
- **FR-015**: System MUST preserve the maintainer's local personal files in place (no deletion, relocation, or overwrite) when building the public export.
- **FR-016**: System MUST provide a gitignored local-path configuration so the maintainer's workspace continues resolving to personal resume, job list, contact, and artifact paths after publish.
- **FR-017**: System MUST publish to a **separate** public GitHub repository via allowlist-based export—not by making the private working repository public.

### Key Entities

- **Public Repository**: The open-source GitHub project; attributes include name, description, visibility, default branch, and root README.
- **Sanitization Policy**: Rules defining excluded vs included paths and content transformations before publish.
- **Template Bundle**: Sanitized sample files (base resume, job opportunities, role reference, contact config) replacing author-specific data.
- **Publish Checklist**: Verifiable gate executed before initial push and documented for future contributors.
- **Reproduction Guide**: README sections mapping setup and pilot steps to multiple AI tool environments.
- **Workflow Contract**: Published schemas for resume markdown, cover letters, manifests, and file naming—tool-agnostic data shapes.
- **Local-Only Data**: User-specific files that must never enter the public repository (real resume, real applications, credentials).
- **Local Path Configuration**: Gitignored mapping from workflow entry points to the maintainer's personal file locations.
- **Publish Staging Tree**: Ephemeral or regenerable directory containing only allowlisted open-source files before GitHub push.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of items on the pre-publish checklist pass before the first public push (zero blocked categories remain in the staging tree).
- **SC-002**: A fresh clone contains zero detected secrets and zero author PII in tracked files, verified by documented scan steps and manual spot-check of contact and config files.
- **SC-003**: A new user following only the README completes the single-role pilot (tailored resume + cover letter as PDF) in under 90 minutes without maintainer assistance.
- **SC-004**: README includes distinct, complete setup subsections for at least three AI tool environments: Cursor (with Spec Kit), Claude Code, and Codex (or documented equivalents).
- **SC-005**: At least one sample job opportunity and one sample base resume ship with the repository, enabling pilot execution without external data files.
- **SC-006**: 100% of functional requirements FR-001 through FR-014 are traceable to a README section, template file, or published contract in the repository.
- **SC-007**: Community adopters can locate how to configure personal data locally, optional cloud upload, and PDF conversion each within 2 minutes of reading the README table of contents.
- **SC-008**: Repository receives a clear one-paragraph description on GitHub explaining that it is an AI-agent-driven job application toolkit, accurate to included scope.
- **SC-009**: After publish, the maintainer completes one personal batch re-run using unchanged local files with zero manual path rewiring beyond documented one-time `local-paths.json` setup.

## Assumptions

- **Repository host**: GitHub is the target platform; creation uses the maintainer's connected GitHub integration (personal account unless an organization is specified later).
- **Default visibility**: Public repository for true open-source distribution.
- **Default license**: MIT License unless the maintainer selects a different OSI-approved license before publish.
- **Source scope**: The workflow to bottle up comprises Spec Kit features `001-beast-ai-resume` and `002-tailored-job-applications`, associated artifacts structure, cursor rules, agent skills, and batch tooling—not unrelated local files (`google_scopes.md`, personal job opportunity lists, Cisco role reference with author-specific content unless sanitized).
- **Clean history**: Initial public push uses a clean commit history without prior secret commits; if the local repo history is contaminated, history rewriting or fresh export is in scope for implementation.
- **MCP as optional**: Google Drive, GitHub, and LinkedIn MCP servers enhance the workflow but README documents a minimal path without them.
- **Tool parity**: Claude Code and Codex sections describe skill/rule placement and prompt workflows analogous to Cursor; exact UI may differ but outcomes must match.
- **No live job scraping**: Open-source toolkit documents using a user-maintained job opportunities markdown file; automated scraping is out of scope.
- **Author attribution**: README may credit the original author as maintainer without embedding PII in config templates; maintainer GitHub username in README is acceptable.
- **Implementation timing**: This specification defines *what* to publish; repository creation and content curation happen in `/speckit-plan` and `/speckit-implement` phases.
