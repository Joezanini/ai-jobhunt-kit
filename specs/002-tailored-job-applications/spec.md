# Feature Specification: Batch Tailored Job Application Artifacts

**Feature Branch**: `002-tailored-job-applications`

**Created**: 2026-06-27

**Status**: Draft

**Input**: User description: "I want to iterate through every job listed in sf_bay_area_job_opportunities.md and create a ATS friendly resume for each position. I want all information to be accurate, but catered to each role individually. I also want a cover letter created for each role. I want all artifacts in PDF format in Google Drive using the Drive MCP server. I want naming for all files to be specific to each position."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate Tailored Resume for Each Target Role (Priority: P1)

Joe runs a batch process against every job opportunity documented in `sf_bay_area_job_opportunities.md`. For each role, the system produces a single-column, ATS-friendly resume that highlights honest alignment with that role's requirements—reframing experience and keywords without fabricating employers, titles, dates, or accomplishments.

**Why this priority**: The resume is the primary gate for ATS and recruiter screening; without role-specific resumes, the batch has no core value.

**Independent Test**: Select any three roles from the source list (e.g., Fractional AI DevRel, Anthropic Claude Code Specialist, Neo4j Senior Developer Advocate). For each, verify the resume contains posting-relevant keywords in context, every bullet traces to `joe_zanini_resume.md` or other verified sources, and no two resumes are identical copy-paste.

**Acceptance Scenarios**:

1. **Given** the job opportunities source file and Joe's base resume, **When** the batch completes, **Then** one tailored resume exists for every in-scope role (20 unique positions across Top Matches, Additional Strong Options, and Borderline sections).
2. **Given** any generated resume, **When** a reviewer compares it to the corresponding job summary in the source file, **Then** headline, summary, skills, and experience bullets reflect that role's emphasis (e.g., AI enablement vs. OSS community vs. partner architecture) without invented credentials.
3. **Given** Joe's confirmed employment timeline (Qualys ended March 2022; Webex began March 2022), **When** any resume is reviewed, **Then** dates and titles match verified facts and overlapping "Present" entries from the source resume are corrected.
4. **Given** roles flagged as technical stretches in the source file (e.g., IBM watsonx.data, NVIDIA distributed training), **When** the resume is read, **Then** honest framing is preserved—strengths emphasized, gaps not concealed, and no false claims of deep expertise in unverified domains.

---

### User Story 2 - Generate Role-Specific Cover Letter for Each Position (Priority: P2)

For each in-scope role, the system produces a cover letter that connects Joe's verifiable experience to that company's stated needs, references the specific role title and company, and complements (not duplicates) the tailored resume.

**Why this priority**: Cover letters differentiate applications for competitive DevRel and AI enablement roles where narrative fit matters after ATS pass-through.

**Independent Test**: For any role, confirm the cover letter names the company and role, cites 2–3 concrete achievements from verified experience, addresses at least one priority requirement from the job summary, and fits within one page when rendered to PDF.

**Acceptance Scenarios**:

1. **Given** a completed tailored resume for a role, **When** the cover letter is generated, **Then** it references the same company and job title and does not contradict resume facts.
2. **Given** roles with special constraints noted in the source file (e.g., U.S. citizenship required for OpenAI Government Support), **When** the cover letter is produced, **Then** it either addresses eligibility honestly or includes a visible note in the batch summary that manual review is required before submission.
3. **Given** roles with unposted salary or recruiting-firm intermediaries (e.g., Fractional AI, Kinora Group), **When** the cover letter is produced, **Then** it remains professional without inventing compensation figures or undisclosed employer names beyond what the source file states.

---

### User Story 3 - Deliver PDF Artifacts to Google Drive with Position-Specific Names (Priority: P3)

All resumes and cover letters are converted to PDF and uploaded to Joe's Google Drive. Each file name uniquely identifies the candidate, document type, company, and role so Joe can locate and submit the correct packet per application without ambiguity.

**Why this priority**: PDF is the standard submission format; centralized Drive storage enables review, sharing, and mobile access before applications are submitted.

**Independent Test**: After batch completion, open Google Drive and confirm 40 PDF files exist (20 resumes + 20 cover letters), each openable as a valid PDF, named per the naming convention, and organized under a single dedicated application folder.

**Acceptance Scenarios**:

1. **Given** a completed batch run, **When** Joe browses the designated Drive folder, **Then** every in-scope role has exactly two PDF files: one resume and one cover letter.
2. **Given** any uploaded file, **When** the file name is inspected, **Then** it follows the pattern `{LastName}_{FirstName}_{DocumentType}_{Company}_{RoleSlug}.pdf` (e.g., `Zanini_Joe_Resume_FractionalAI_DeveloperRelationsEngineer.pdf`) with no generic or duplicate names across roles.
3. **Given** a PDF is downloaded from Drive, **When** opened, **Then** content matches the tailored source document, renders on letter-size pages without broken layout, and resume length is 1–2 pages.

---

### User Story 4 - Batch Progress and Error Recovery (Priority: P4)

Joe can see which roles succeeded or failed during batch processing and re-run individual roles without regenerating the entire batch.

**Why this priority**: With 20 roles and 40 artifacts, partial failures (Drive upload, missing posting detail) must not force a full restart.

**Independent Test**: Simulate a failure on one role mid-batch; confirm completed roles retain their Drive artifacts, the failure is logged with role identifier, and re-processing that single role produces the missing PDFs without overwriting unrelated files.

**Acceptance Scenarios**:

1. **Given** a batch run in progress, **When** it completes, **Then** a summary lists each role with status (success, skipped, failed) and file names produced.
2. **Given** a failed role, **When** Joe triggers re-processing for that role only, **Then** only that role's resume and cover letter are regenerated and re-uploaded.

---

### Edge Cases

- **Insufficient job detail**: Three borderline roles (Vercel, Glean, Everlaw) appear only as table summaries in the source file. Tailoring uses available summary text; batch summary flags these for Joe to verify against live postings before applying.
- **Duplicate company, different roles**: Anthropic has three distinct roles—each must produce separate resume/cover letter pairs with role-specific naming (not company-only names).
- **Recruiting-firm postings**: Kinora Group lists a client role without naming the end employer; file names use Kinora Group and role title as documented.
- **Hard eligibility filters**: OpenAI AI Support Engineer, Government requires U.S. citizenship—artifacts are still generated, but batch summary flags the constraint for Joe's decision.
- **Technical stretch roles**: AMD, NVIDIA, IBM roles note significant domain gaps—resumes remain honest; cover letters may acknowledge growth areas without underselling core DevRel/partner strengths.
- **Drive naming collisions**: If a file with the same name already exists, the system appends a date suffix or version indicator rather than silently overwriting.
- **ATS formatting**: Resumes avoid tables, columns, headers/footers, images, and special characters that commonly break ATS parsers.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST process every unique job opportunity in `sf_bay_area_job_opportunities.md`—15 numbered role sections plus 5 borderline table entries (20 roles total).
- **FR-002**: System MUST use `joe_zanini_resume.md` as the authoritative source for contact information, employment history, education, and skills unless superseded by verified clarifications from prior work (e.g., Qualys end date March 2022).
- **FR-003**: System MUST tailor each resume to the corresponding role's job summary, responsibilities, and stated fit rationale in the source file, including natural use of role-relevant keywords for ATS compatibility.
- **FR-004**: System MUST NOT fabricate employers, job titles, employment dates, degrees, certifications, compensation, or accomplishments not supported by verified sources.
- **FR-005**: System MUST produce one cover letter per in-scope role that is unique to that company and position.
- **FR-006**: System MUST deliver all resumes and cover letters as PDF files uploaded to the user's Google Drive account.
- **FR-007**: System MUST store all artifacts in a single dedicated Drive folder named for this job search batch (e.g., `Alex Rivera - SF Bay Area Applications 2026`).
- **FR-008**: System MUST name each file to uniquely identify document type, company, and role title; no two files may share the same name.
- **FR-009**: System MUST format resumes for ATS compatibility: single column, standard section headings, plain text-friendly structure, no multi-column layouts or graphics.
- **FR-010**: System MUST correct known resume inaccuracies from the source resume (overlapping Qualys/Webex "Present" dates) in every generated artifact.
- **FR-011**: System MUST produce a batch completion summary listing each role, generated file names, Drive paths, and any warnings (eligibility constraints, stretch roles, thin source data).
- **FR-012**: System MUST support re-processing individual roles without regenerating the full batch.
- **FR-013**: System MUST preserve moderate, honest AI/LLM language—reframing verifiable automation, bots, ML, and hands-on AI tool use without implying enterprise LLM platform leadership Joe has not held.

### Key Entities

- **Job Opportunity**: A target position from the source file; attributes include company, role title, location, work model, salary range (if posted), job summary, fit notes, LinkedIn URL, and eligibility flags.
- **Source Resume**: Joe's canonical resume markdown; base facts for all tailored outputs.
- **Tailored Resume**: Role-specific resume derived from source resume + job opportunity; one per role.
- **Cover Letter**: Role-specific narrative document; one per role; complements the tailored resume.
- **Application Artifact**: A PDF file (resume or cover letter) ready for submission; linked to exactly one job opportunity.
- **Batch Run**: A single execution that processes all or a subset of job opportunities and records per-role status.
- **Drive Folder**: Container in Google Drive holding all artifacts for this job search batch.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of in-scope roles (20/20) have both a tailored resume PDF and cover letter PDF in Google Drive after a successful batch run.
- **SC-002**: 100% of generated file names are unique and include company and role identifiers discernible without opening the file.
- **SC-003**: A reviewer can match any PDF to its target posting within 10 seconds using file name alone.
- **SC-004**: For a random sample of 5 roles, every resume bullet traces to a verifiable fact in the source resume or documented clarifications—with zero fabricated claims found.
- **SC-005**: For a random sample of 5 roles, each tailored resume contains at least 5 keywords or phrases aligned with that role's posting summary, used in meaningful context (not isolated keyword lists).
- **SC-006**: All resume PDFs render at 1–2 pages; all cover letter PDFs render at 1 page or fewer.
- **SC-007**: Joe can locate the full application packet for any role in under 1 minute using the Drive folder structure and naming convention.
- **SC-008**: Batch completion summary is available showing success/failure per role, enabling Joe to identify and re-run any failed items within one follow-up action.

## Assumptions

- **Scope**: All 20 unique roles in `sf_bay_area_job_opportunities.md` are in scope—15 fully detailed sections plus 5 borderline table entries (Box, Vercel, Mesh, Glean, Everlaw). Roles appearing in both numbered sections and the borderline table are counted once.
- **Source of truth**: `joe_zanini_resume.md` is the primary factual base; `cisco_role_reference.md`, prior spec clarifications (`001-beast-ai-resume`), and `sf_bay_area_job_opportunities.md` provide supplemental verified context.
- **Honesty standard**: Same standard as prior resume work—accurate but strategically framed; stretch roles are addressed honestly, not declined.
- **Google Drive access**: Joe's Google Drive is accessible via the connected Drive integration; a new subfolder will be created for this batch unless an existing folder is specified later.
- **PDF format**: PDF is the required delivery format per user request; brief intermediate markdown may be used during generation but is not the final deliverable.
- **Cover letter tone**: Professional, concise, first-person; one page; no salary negotiation unless posting invites it.
- **Submission**: This feature produces application materials only; actual job submission via LinkedIn or company portals is out of scope.
- **Live posting verification**: LinkedIn URLs in the source file are references for Joe; the batch uses summaries in the markdown file and does not require live scraping for v1.
- **Borderline thin data**: For Vercel, Glean, and Everlaw (table-summary only), tailoring uses available text; Joe should verify against live postings before submitting.
