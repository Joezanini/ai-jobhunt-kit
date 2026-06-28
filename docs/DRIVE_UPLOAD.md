# Google Drive Upload (MCP)

Upload tailored PDF resumes and cover letters to Google Drive using the Drive MCP server.

**Prerequisites**: PDFs generated locally; [MCP_SETUP.md](./MCP_SETUP.md) Drive section done.

## Step 1: Verify authentication

```
Tool: authGetStatus (user-drive)
```

Expected: connected with Drive scope available.

If failing, run `authListScopes` and re-authenticate per server docs.

## Step 2: Create batch folder

```
Tool: createFolder
Arguments:
  name: "<drive_folder_name from local-paths.json>"
```

Record returned folder ID as `drive_folder_id` in `artifacts_root/batch/manifest.json`.

## Step 3: Name files

Follow `specs/002-tailored-job-applications/contracts/file-naming-convention.md`:

```text
{LastName}_{FirstName}_{DocumentType}_{Company}_{RoleSlug}.pdf
```

Read `candidate_name` from `local-paths.json`—do not hard-code names in scripts.

## Step 4: Upload each PDF

```
Tool: uploadFile
Arguments:
  localPath: "/absolute/path/to/artifacts/.../pdf/role-id_resume.pdf"
  name: "Rivera_Alex_Resume_ExampleCo_DeveloperRelations.pdf"
  parentFolderId: "<drive_folder_id>"
```

Repeat for cover letters (`CoverLetter` document type).

## Step 5: Verify

```
Tool: listFolder
Arguments:
  folderId: "<drive_folder_id>"
```

Confirm file count matches manifest (2 PDFs per role).

## Step 6: Update manifest

Set per-role `status` to `uploaded`; record `resume_pdf` and `cover_letter_pdf` file names.

## Collision handling

If a file name already exists in Drive, append `_YYYYMMDD` before `.pdf` (see batch README).

## Minimal path (no Drive MCP)

Keep PDFs in `artifacts_root/pdf/` and upload manually via drive.google.com. Core workflow still delivers value (FR-014).

## Next step

Review packet before submitting on company career sites or LinkedIn Easy Apply.
