# Feature Specification: Beast AI Enablement Lead Tailored Resume

**Feature Branch**: `001-beast-ai-resume`

**Created**: 2026-06-25

**Status**: Draft

**Input**: User description: "I need a tailored resume that will best land the job posting listed at AI_Enablement_Lead.md. I want to be honest but not get filtered by apps that are looking for keywords or disqualifying language. Use my current resume joe_zanini_resume.md and anything else known about me. Output in markdown for easy PDF conversion."

## Clarifications

### Session 2026-06-25

- Q: When did Qualys employment end relative to Webex (March 2022)? → A: Qualys ended March 2022 when Webex started.
- Q: What headline format appears directly under your name? → A: Descriptive tagline (not a job title); exact employer titles remain in Experience section.
- Q: How bold should AI/LLM language be across the resume? → A: Moderate — reframe verifiable automation/ML/bot work with posting-aligned language; note hands-on AI tool experimentation honestly without implying enterprise LLM leadership.
- Q: Which AI work examples should the companion document feature for the application? → A: Webex Python SDK / technical content plus personal Spec Kit / agentic tooling (this repository).
- Q: Should relocation willingness appear on the resume? → A: No mention on resume; handle in application or cover letter if needed.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Pass ATS and Recruiter Screen (Priority: P1)

Joe applies to the Beast Industries AI Enablement Lead role by submitting a tailored resume (and later, separate AI work samples per the posting). The resume must surface his strongest honest alignment with a builder-first, embedded enablement role—without being discarded by keyword filters or raising red flags from inflated claims.

**Why this priority**: If the resume fails automated screening or a 30-second human scan, no other tailoring matters.

**Independent Test**: Run the resume text against the role's required and bonus keywords from `AI_Enablement_Lead.md`; confirm each appears in context tied to verifiable experience. Have a reviewer unfamiliar with Joe identify his fit for "embedded co-builder" vs "trainer/PM" within 30 seconds.

**Acceptance Scenarios**:

1. **Given** the Beast job posting requirements, **When** a reviewer scans the resume headline, tagline, and summary, **Then** they see explicit alignment with AI enablement, hands-on building, and cross-functional embedding—not a generic developer-relations profile or a fabricated job title.
2. **Given** an ATS keyword scan, **When** the resume is compared to the posting, **Then** it includes natural occurrences of terms such as AI, automation, workflows, LLMs/agents (where truthful), prompt engineering, evaluation, and stakeholder communication without keyword stuffing.
3. **Given** Joe's source resume, **When** each bullet in the tailored resume is checked, **Then** every claim traces to verifiable experience with no fabricated titles, employers, or shipped AI products.

---

### User Story 2 - Reframe Experience for the Role's Philosophy (Priority: P2)

The resume reframes Joe's Webex Developer Relations and Qualys Technical Account Management experience to match Beast's stated philosophy: enablement happens by building together, not by running training programs or writing curricula.

**Why this priority**: The posting explicitly rejects a "training program" profile. Joe's dev-rel and TAM work is a strong honest match if framed as co-building and adoption through shipped outcomes.

**Independent Test**: A reader can articulate how Joe embedded with teams, co-built integrations/tools, and left others able to maintain improvements—without describing him primarily as a classroom trainer or curriculum author.

**Acceptance Scenarios**:

1. **Given** Joe's Webex Partner Engineer role, **When** experience bullets are read, **Then** they emphasize guiding builders from ideation through shipped integrations, SDK/tooling ownership, and workflow automation—not only "community support."
2. **Given** Joe's Qualys TAM and team-lead experience, **When** experience bullets are read, **Then** they emphasize hands-on solution adoption with security and IT stakeholders, demos, onboarding, and enabling non-technical teams—without leading with "trained new hires" as the primary value prop.
3. **Given** Joe's data science and ML labeling background, **When** the education/skills sections are read, **Then** they establish credible foundation in data, evaluation, and applied ML without overstating current production LLM engineering scope.

---

### User Story 3 - Produce a PDF-Ready Markdown Deliverable (Priority: P3)

Joe receives a single markdown resume file structured for clean conversion to PDF (single-column, standard headings, no complex tables or HTML) so he can submit quickly with the required AI work examples.

**Why this priority**: Format friction should not delay application; the posting asks for resume plus 1–2 AI work samples as separate artifacts.

**Independent Test**: Convert the markdown file to PDF using a standard tool; output fits 1–2 pages, preserves hierarchy, and remains readable without manual reformatting.

**Acceptance Scenarios**:

1. **Given** the delivered markdown file, **When** converted to PDF, **Then** contact information, section order, and bullet hierarchy render correctly on letter-size output.
2. **Given** the posting's application instructions, **When** Joe prepares his packet, **Then** the resume stands alone while a separate short list of 1–2 AI work example links/descriptions is documented in the spec's companion guidance (not embedded as unverifiable resume bullets).

---

### Edge Cases

- **Overlapping employment dates**: Source resume lists both roles as "Present"; confirmed Qualys ended March 2022 when Webex began. Tailored resume MUST show Qualys as June 2020 – March 2022 and Webex as March 2022 – Present.
- **Limited explicit LLM production experience**: Resume uses moderate AI/LLM language—tied to verifiable automation, bots, ML/data roles, and SDK/tooling in experience bullets; summary and skills may note hands-on experimentation with modern AI tools. Must NOT imply Joe led enterprise LLM deployments or platform architecture.
- **Webex-centric bio**: Current bio focuses entirely on Webex Developer community; tailored version must speak to cross-company AI enablement and builder partnerships.
- **Disqualifying language**: Avoid phrases that signal misalignment (e.g., "curriculum design," "L&D program owner," "managed training calendar") unless reframed as co-built adoption outcomes.
- **Geography/relocation**: Posting offers relocation assistance; resume will NOT mention relocation (confirmed). Address in application or cover letter if desired.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Deliverable MUST be a markdown resume file at `joe_zanini_resume_beast_ai_enablement.md` in the project root (sibling to `joe_zanini_resume.md`).
- **FR-002**: Resume MUST retain accurate contact information, education, and employer names from the source resume. Resume MUST NOT include relocation language in the header or contact block.
- **FR-003**: Resume MUST include a descriptive tagline directly under the name (not a fabricated job title), signaling technical enablement and AI workflow building; exact employer titles (e.g., Developer Relations Engineer) MUST appear only in the Experience section.
- **FR-003a**: Resume MUST include a rewritten professional summary (3–5 sentences) below the tagline, targeting AI Enablement Lead at Beast: builder-first embedding, workflow automation, cross-functional trust-building, and measurable adoption—not generic dev-rel positioning.
- **FR-004**: Resume MUST reorder and rewrite experience bullets so Webex Developer Relations is the primary recent role, with bullets mapped to posting themes: co-building workflows/tools, developer and partner enablement through shipping, content and public technical presence, product feedback loops, and automation/bots/API integrations.
- **FR-005**: Resume MUST present Qualys experience as June 2020 – March 2022, emphasizing solutions engineering, executive-facing demos, customer onboarding, and enabling non-technical teams on complex tooling.
- **FR-006**: Resume MUST include Bonfire and Dor Technologies roles with bullets emphasizing data analysis, ML training data, evaluation-minded work, and programmatic data collection—supporting credibility for measurement and AI quality themes without inventing LLM projects.
- **FR-007**: Resume MUST include a Skills section grouped for ATS and human scan: AI & Automation (LLMs, agents, prompt engineering, evaluation, workflow automation), Engineering (Python, JavaScript, APIs, OAuth), and Enablement (developer relations, technical advocacy, cross-functional collaboration, technical writing/talks).
- **FR-008**: Resume MUST incorporate posting keywords naturally at least once each where truthful (moderate calibration): AI, automation, workflows, tools, embed/partner, productivity, measurement or impact, non-technical stakeholders, self-directed, experimentation—reframing verifiable experience with posting-aligned language without overstating LLM production scope.
- **FR-009**: Resume MUST NOT fabricate job titles, employers, certifications, or shipped AI products Joe has not built.
- **FR-010**: Resume MUST NOT use keyword stuffing (repeated identical phrases, invisible text, or skills lists disconnected from experience).
- **FR-011**: Resume MUST be formatted for PDF export: H1 name, descriptive tagline line, plain contact line, `##` section headers, bullet lists only (no tables required), target length 1–2 pages when rendered.
- **FR-012**: Companion document `ai_work_examples_beast.md` MUST feature exactly these two application examples: (1) Webex Python SDK stewardship and/or related technical content (blogs, talks), and (2) personal Spec Kit / agentic tooling work from this repository—each with a short description and link or path where verifiable.
- **FR-013**: Resume MUST surface bonus-fit signals honestly where applicable: developer relations background, solutions-adjacent TAM work, public technical content, open-source/SDK administration.

### Key Entities

- **Source Resume** (`joe_zanini_resume.md`): Canonical facts for employment, education, contact, and skills inventory.
- **Target Job Posting** (`AI_Enablement_Lead.md`): Role responsibilities, required traits, bonus points, and application instructions.
- **Tailored Resume** (`joe_zanini_resume_beast_ai_enablement.md`): Primary deliverable; markdown optimized for ATS and Beast hiring philosophy.
- **AI Work Examples Annex**: Short markdown companion (`ai_work_examples_beast.md`) listing the two confirmed application examples—Webex Python SDK/technical content and personal Spec Kit/agentic tooling—kept separate from resume bullets to maintain honesty and brevity.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of employment entries use dates that are internally consistent (no unexplained dual full-time "Present" roles).
- **SC-002**: At least 12 of 15 core terms from the posting's "What We're Looking For" and "What You'll Do" sections appear naturally in the tailored resume (AI, embed/co-build, automation, workflows, tools, LLM/agent terminology where honest, prompt engineering, evaluation, deployment/shipping, non-technical communication, self-directed, productivity/impact measurement, cross-functional).
- **SC-003**: A blind reviewer can correctly identify Joe's primary fit as "developer relations / embedded technical enablement" in under 30 seconds, with secondary fit as "solutions-oriented adoption with non-technical teams."
- **SC-004**: Resume renders to a 1–2 page PDF without structural breakage (headers, bullets, contact line intact).
- **SC-005**: Zero resume bullets fail a traceability check back to source resume facts or documented assumptions in this spec.
- **SC-006**: Companion AI work examples document provides exactly 2 concrete artifacts: Webex Python SDK/technical content and personal Spec Kit/agentic tooling from this repository, each with description and verifiable link or reference.

## Assumptions

- Qualys employment ended March 2022 when Webex began (confirmed).
- Joe has hands-on familiarity with modern AI tooling (LLM chat interfaces, agentic coding assistants, workflow automation) through professional experimentation and personal projects. Resume uses **moderate** AI language: reframes verifiable automation/ML/bot work with posting-aligned terms; does not claim enterprise LLM platform leadership.
- Joe is open to relocation per the posting's relocation assistance, but relocation will not appear on the resume (confirmed); address in application or cover letter if desired.
- Webex role includes legitimate automation/bot/API integration work and SDK administration that supports "built tools others can maintain" narrative without inventing internal LLM products.
- Application will include AI work examples as separate artifacts; the resume itself stays concise and factual.
- No additional employment history beyond `joe_zanini_resume.md` is available unless Joe adds it later.
- LinkedIn URL on resume remains as plain text "LinkedIn" unless Joe provides a full URL for the tailored version.
