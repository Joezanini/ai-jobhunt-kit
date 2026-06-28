#!/usr/bin/env python3
"""Convert markdown resumes and cover letters to PDF with clickable links."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import markdown
from xhtml2pdf import pisa

CSS = """
@page { size: letter; margin: 0.75in; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.35; color: #111; }
h1 { font-size: 16pt; margin-bottom: 0.2em; }
h2 { font-size: 12pt; margin-top: 0.9em; margin-bottom: 0.3em; border-bottom: 1px solid #ccc; }
h3 { font-size: 11pt; margin-top: 0.6em; margin-bottom: 0.15em; }
p { margin: 0.4em 0; }
ul { margin: 0.2em 0 0.4em 1.1em; padding: 0; }
li { margin-bottom: 0.15em; }
strong { font-weight: bold; }
a { color: #0563c1; text-decoration: underline; }
"""

MD_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")
URL_RE = re.compile(r"(?<![\(\"])(https://[^\s<>]+)")
EMAIL_RE = re.compile(r"(?<![\w.@])([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?![\w.])")


def load_paths(paths_file: Path) -> dict:
    data = json.loads(paths_file.read_text(encoding="utf-8"))
    root = paths_file.parent
    artifacts = Path(data["artifacts_root"])
    if not artifacts.is_absolute():
        artifacts = root / artifacts
    contact_path = Path(data["contact"])
    if not contact_path.is_absolute():
        contact_path = root / contact_path
    contact = json.loads(contact_path.read_text(encoding="utf-8"))
    return {
        "artifacts_root": artifacts,
        "contact": contact,
        "candidate_name": data["candidate_name"],
    }


def phone_regex(contact: dict) -> re.Pattern[str] | None:
    phone = contact.get("phone")
    if not phone:
        return None
    escaped = re.escape(phone)
    return re.compile(rf"(?<!\d)({escaped})(?!\d)")


def autolink_plain_urls(text: str, phone_re: re.Pattern[str] | None, phone_tel: str | None) -> str:
    placeholders: list[str] = []

    def protect(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"@@MDLINK{len(placeholders) - 1}@@"

    text = MD_LINK_RE.sub(protect, text)

    def wrap_url(match: re.Match[str]) -> str:
        url = match.group(1).rstrip(".,;)")
        return f"[{url}]({url})"

    def wrap_email(match: re.Match[str]) -> str:
        email = match.group(1)
        return f"[{email}](mailto:{email})"

    def wrap_phone(match: re.Match[str]) -> str:
        display = match.group(1)
        tel = phone_tel or display
        return f"[{display}](tel:{tel})"

    text = URL_RE.sub(wrap_url, text)
    text = EMAIL_RE.sub(wrap_email, text)
    if phone_re:
        text = phone_re.sub(wrap_phone, text)

    for i, link in enumerate(placeholders):
        text = text.replace(f"@@MDLINK{i}@@", link)
    return text


def md_to_pdf(md_path: Path, pdf_path: Path, phone_re: re.Pattern[str] | None, phone_tel: str | None) -> None:
    text = md_path.read_text(encoding="utf-8")
    text = autolink_plain_urls(text, phone_re, phone_tel)
    html_body = markdown.markdown(text, extensions=["extra", "sane_lists", "smarty"])
    html = (
        f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{html_body}</body></html>"
    )
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pdf_path, "wb") as out:
        status = pisa.CreatePDF(html, dest=out, encoding="utf-8")
        if status.err:
            raise RuntimeError(f"PDF failed for {md_path}")


def drive_name(last: str, first: str, doc_type: str, company_slug: str, role_slug: str) -> str:
    return f"{last}_{first}_{doc_type}_{company_slug}_{role_slug}.pdf"


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert batch markdown to PDF")
    parser.add_argument(
        "--paths",
        type=Path,
        default=Path("local-paths.json"),
        help="Path to local-paths.json",
    )
    args = parser.parse_args()
    cfg = load_paths(args.paths.resolve())
    artifacts = cfg["artifacts_root"]
    manifest_path = artifacts / "batch" / "manifest.json"
    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        sys.exit(1)

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    roles = {r["role_id"]: r for r in manifest["roles"]}
    pdf_dir = artifacts / "pdf"
    resumes = artifacts / "resumes"
    cover_letters = artifacts / "cover-letters"
    contact = cfg["contact"]
    phone_re = phone_regex(contact)
    phone_tel = contact.get("phone_tel")
    name = cfg["candidate_name"]

    for md_path in sorted(resumes.glob("*.md")):
        role_id = md_path.stem
        role = roles.get(role_id)
        if not role:
            continue
        local = pdf_dir / f"{role_id}_resume.pdf"
        md_to_pdf(md_path, local, phone_re, phone_tel)
        role["resume_pdf_local"] = str(local)
        role["resume_pdf"] = drive_name(
            name["last"], name["first"], "Resume", role["company_slug"], role["role_slug"]
        )
        role["status"] = "generated"
        print(f"resume: {role_id}")

    for md_path in sorted(cover_letters.glob("*.md")):
        role_id = md_path.stem
        role = roles.get(role_id)
        if not role:
            continue
        local = pdf_dir / f"{role_id}_cover_letter.pdf"
        md_to_pdf(md_path, local, phone_re, phone_tel)
        role["cover_letter_pdf_local"] = str(local)
        role["cover_letter_pdf"] = drive_name(
            name["last"], name["first"], "CoverLetter", role["company_slug"], role["role_slug"]
        )
        print(f"cover: {role_id}")

    manifest["roles"] = list(roles.values())
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Done: {len(list(pdf_dir.glob('*.pdf')))} PDFs")


if __name__ == "__main__":
    main()
