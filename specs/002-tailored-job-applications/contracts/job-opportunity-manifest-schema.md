# Contract: Job Opportunity Manifest Schema

**Version**: 1.0.0 | **Feature**: `002-tailored-job-applications`

## Purpose

Defines the JSON manifest at `artifacts/002-tailored-job-applications/batch/manifest.json` listing all in-scope roles for batch processing, naming, and re-runs.

## Schema

```json
{
  "batch_version": "1.0.0",
  "source_file": "sf_bay_area_job_opportunities.md",
  "drive_folder_name": "Alex Rivera - SF Bay Area Applications 2026",
  "drive_folder_id": null,
  "roles": [
    {
      "role_id": "fractional-ai-devrel",
      "company": "Fractional AI",
      "company_slug": "FractionalAI",
      "title": "Developer Relations Engineer",
      "role_slug": "DeveloperRelationsEngineer",
      "location": "San Francisco, CA",
      "work_model": "On-site",
      "salary_range": "Not posted",
      "linkedin_url": "https://www.linkedin.com/jobs/view/4418995962/",
      "category": "devrel",
      "warnings": [],
      "keyword_targets": ["developer relations", "technical content", "open source", "conferences", "engineering"],
      "status": "pending"
    }
  ]
}
```

## Field Rules

| Field | Required | Notes |
|-------|----------|-------|
| `role_id` | yes | Unique kebab-case identifier |
| `company_slug` | yes | No spaces; used in file names |
| `role_slug` | yes | PascalCase words concatenated; no punctuation |
| `category` | yes | One of: `devrel`, `ai_enablement`, `partner_gtm`, `engineering`, `stretch`, `support_alt` |
| `warnings` | no | Array of WarningFlag values from data-model.md |
| `keyword_targets` | yes | Minimum 5 strings |
| `status` | yes | `pending`, `generated`, `uploaded`, `failed`, `skipped` |

## Complete role_id List

All 20 entries MUST be present. Canonical list in [research.md](../research.md) R1 table.
