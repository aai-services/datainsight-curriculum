"""Automatic checks for Project 2: Compare two groups.

These confirm the project is complete. Peer review judges whether it is good.
Run locally with:  pytest
"""
import re

import pytest

from harness import run_full
from project_common import ROOT, charts, load, markdown_text, sections, word_count

SECTIONS = ["Question", "Data", "Method", "Results", "Interpretation", "Limitations", "Reflection"]
MAX_DATA_BYTES = 5_000_000


def test_sections_present():
    missing = [s for s in SECTIONS if s not in sections(load())]
    assert not missing, "Keep these section headings in project.ipynb: " + ", ".join(missing)


def test_no_todo_left():
    left = [c.source.strip().splitlines()[0][:50] for c in load().cells if "TODO" in c.source]
    assert not left, "Replace the TODO text in the cells starting: " + " | ".join(left)


def test_source_and_license():
    data = markdown_text(load(), "Data")
    assert re.search(r"Source:\s*\S*https?://\S+", data), "In the Data section, give 'Source:' followed by a link."
    lic = re.search(r"License:\s*(\S.*)", data)
    assert lic and len(lic.group(1).strip()) >= 3, "In the Data section, give 'License:' followed by the license."


def test_interpretation_length_and_numbers():
    text = markdown_text(load(), "Interpretation")
    n = word_count(text)
    assert 150 <= n <= 400, f"The Interpretation has {n} words; it should have 150 to 400."
    assert len(re.findall(r"\d[\d,.]*", text)) >= 3, "Report the difference and both ends of its interval as numbers."


def test_limitations_length():
    n = word_count(markdown_text(load(), "Limitations"))
    assert n >= 50, f"The Limitations section has {n} words; write at least 50."


def test_data_committed():
    files = [p for p in (ROOT / "data").glob("*") if p.is_file() and p.name != "README.md"]
    assert files, "Add your data file to the data folder."
    big = [p.name for p in files if p.stat().st_size > MAX_DATA_BYTES]
    assert not big, "Keep each data file under 5 MB: " + ", ".join(big)


@pytest.fixture(scope="module")
def executed():
    return run_full("project.ipynb", "checks_project.py")


def test_notebook_runs(executed):
    _, _, error = executed
    if error:
        pytest.fail(f"project.ipynb stops with an error at {error}\n"
                    "In Colab, use Runtime, Restart session and run all, and fix the first error.", pytrace=False)


def test_has_a_chart(executed):
    nb, _, error = executed
    if error:
        pytest.skip("The notebook does not run yet.")
    assert charts(nb) >= 1, "Include at least one chart showing both groups (end the chart cell with plt.show())."


def test_results(executed):
    _, results, error = executed
    if error:
        pytest.skip("The notebook does not run yet.")
    failed = [r for r in results if not r["passed"]]
    if failed:
        pytest.fail("\n".join(f"{r['name']}: {r['hint']}" for r in failed), pytrace=False)


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
        "Remove these from your files, then ask the program lead how to clean "
        "your repository history:\n" + "\n".join(found)
    )
