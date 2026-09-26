"""Automatic checks for the Stage 0 tools check.

Run locally with:  pytest -v
"""
import re
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parent.parent

ABOUT_FIELDS = [
    "Name or username",
    "Country",
    "Why I joined",
    "A question I would like to answer with data",
    "What I already know",
]


def about_me():
    return (ROOT / "about-me.md").read_text(encoding="utf-8")


def test_about_me_has_no_todo():
    text = about_me()
    assert "TODO" not in text, "Replace every TODO in about-me.md with your answer."


def test_about_me_fields_answered():
    text = about_me()
    missing = []
    for field in ABOUT_FIELDS:
        m = re.search(rf"\*\*{re.escape(field)}:\*\*[ \t]*(.*)", text)
        if not m or len(m.group(1).strip()) < 2:
            missing.append(field)
    assert not missing, "Answer these lines in about-me.md: " + ", ".join(missing)


def test_about_me_has_no_contact_details():
    text = about_me()
    assert not re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text), "Remove email addresses from about-me.md."
    assert not re.search(r"\+?\d[\d\s().-]{8,}\d", text), "Remove phone numbers from about-me.md."


def test_environment_check_was_run():
    nb = nbformat.read(ROOT / "environment-check.ipynb", as_version=4)
    outputs = [o for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", [])]
    text = " ".join(str(o.get("text", "")) for o in outputs)
    assert "Environment OK" in text, (
        "Run every cell of environment-check.ipynb in Colab, then save it back to "
        "GitHub with File, Save a copy in GitHub."
    )


SECRET_PATTERNS = {
    "Mapbox token": r"\b(?:sk|pk)\.eyJ[A-Za-z0-9._-]{20,}",
    "AWS access key": r"\bAKIA[0-9A-Z]{16}\b",
    "GitHub token": r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "Google API key": r"\bAIza[0-9A-Za-z_-]{35}\b",
    "Slack token": r"\bxox[baprs]-[A-Za-z0-9-]{10,}",
    "OpenAI-style key": r"\bsk-[A-Za-z0-9_-]{20,}",
    "Private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
}


def test_no_secrets_in_repository():
    """Access keys and passwords must never be committed."""
    found = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.stat().st_size > 5_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for name, pattern in SECRET_PATTERNS.items():
            if re.search(pattern, text):
                found.append(f"{path.relative_to(ROOT)}: looks like a {name}")
    assert not found, (
        "Remove these from your files, then ask the Program Director how to clean "
        "your repository history:\n" + "\n".join(found)
    )
