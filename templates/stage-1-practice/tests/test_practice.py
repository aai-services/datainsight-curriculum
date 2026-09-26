"""Automatic checks for the Stage 1 practice notebooks.

Each module is one test. Only the modules you have reached need to pass.
Run locally with:  pytest -v
"""
import re
from pathlib import Path

import pytest

from harness import ROOT, run

MODULES = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]


@pytest.mark.parametrize("module", MODULES)
def test_practice(module):
    results, error = run(f"practice-{module}.ipynb", f"checks_{module.replace('.', '_')}.py")
    if error is not None:
        pytest.fail(
            f"practice-{module}.ipynb stops with an error at {error}\n"
            "In Colab, use Runtime, Restart session and run all, and fix the first error.",
            pytrace=False,
        )
    failed = [r for r in results if not r["passed"]]
    if failed:
        pytest.fail(
            f"{len(results) - len(failed)} of {len(results)} checks passed. Still to do:\n"
            + "\n".join(f"  - {r['name']}: {r['hint']}" for r in failed),
            pytrace=False,
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
