# Batch PDF Conversion

Convert tailored markdown to PDF. Paths come from `local-paths.json` at repo root.

## Prerequisites

```bash
pip install markdown xhtml2pdf
# or: brew install pandoc (alternative below)
```

## Python converter (recommended)

Reads phone/email autolink rules from `contact` in `local-paths.json`:

```bash
cd /path/to/ai-jobhunt-kit
python3 scripts/batch/convert_to_pdf.py --paths local-paths.json
```

Expects manifest at `{artifacts_root}/batch/manifest.json` and markdown under `resumes/` and `cover-letters/`.

## Pandoc alternative

```bash
PATHS=local-paths.json
ARTIFACTS=$(python3 -c "import json; print(json.load(open('$PATHS'))['artifacts_root'])")

pandoc "$ARTIFACTS/resumes/novaai-devrel.md" \
  -o "$ARTIFACTS/pdf/novaai-devrel_resume.pdf"
```

## Single-role re-run

1. Set role `status` to `pending` in manifest.
2. Regenerate markdown.
3. Run `convert_to_pdf.py` again.
4. Upload via [DRIVE_UPLOAD.md](../docs/DRIVE_UPLOAD.md).

## File naming

PDF upload names use `candidate_name` from `local-paths.json` per `specs/002-tailored-job-applications/contracts/file-naming-convention.md`.
