"""Automatic checks for the Stage 0 first data story.

Run locally with:  pytest -v
These checks confirm the story is complete. Peer review judges whether it is good.
"""
import re
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = ROOT / "story.ipynb"
SECTIONS = ["Question", "Data", "Chart", "Story", "Reflection"]
MAX_DATA_BYTES = 5_000_000


def load():
    return nbformat.read(NOTEBOOK, as_version=4)


def sections(nb):
    """Map each '## Section' heading to the text that follows it, up to the next heading."""
    found, current = {}, None
    for cell in nb.cells:
        lines = cell.source.strip().splitlines()
        heading = re.match(r"^##\s+(\w+)", lines[0]) if cell.cell_type == "markdown" and lines else None
        if heading:
            current = heading.group(1)
            found[current] = ["\n".join(lines[1:])]
        elif current:
            found[current].append(cell.source)
    return {k: "\n".join(v) for k, v in found.items()}


def word_count(markdown):
    text = re.sub(r"`[^`]*`|\[([^\]]*)\]\([^)]*\)|[#*_>|-]", r" \1 ", markdown)
    return len(re.findall(r"[A-Za-z0-9\u00C0-\uFFFF']+", text))


def test_all_sections_present():
    missing = [s for s in SECTIONS if s not in sections(load())]
    assert not missing, "Keep these section headings in story.ipynb: " + ", ".join(missing)


def test_no_todo_left():
    left = [i + 1 for i, c in enumerate(load().cells) if "TODO" in c.source]
    assert not left, f"Replace the TODO text in cell(s) {left} of story.ipynb."


def test_data_has_source_and_license():
    data = sections(load()).get("Data", "")
    assert re.search(r"Source:\s*\S*https?://\S+", data), "In the Data section, give 'Source:' followed by a link."
    lic = re.search(r"License:\s*(\S.*)", data)
    assert lic and len(lic.group(1).strip()) >= 3, "In the Data section, give 'License:' followed by the data's license."


def test_story_length():
    n = word_count(sections(load()).get("Story", ""))
    assert 200 <= n <= 400, f"The Story section has {n} words; it should have 200 to 400."


def test_data_files_committed():
    files = [p for p in (ROOT / "data").glob("*") if p.is_file() and p.name != "README.md"]
    assert files, "Add your CSV file to the data folder of your repository."
    big = [f"{p.name} ({p.stat().st_size / 1e6:.1f} MB)" for p in files if p.stat().st_size > MAX_DATA_BYTES]
    assert not big, "Keep each data file under 5 MB: " + ", ".join(big)


@pytest.fixture(scope="module")
def executed():
    """Run the notebook from top to bottom, as a reader would."""
    nb = load()
    try:
        NotebookClient(nb, timeout=300, kernel_name="python3",
                       resources={"metadata": {"path": str(ROOT)}}).execute()
    except CellExecutionError as err:
        return nb, f"{err.ename}: {err.evalue}"
    return nb, None


def test_notebook_runs(executed):
    _, error = executed
    assert error is None, (
        "story.ipynb stops with an error when run from the top:\n" + str(error) +
        "\nIn Colab, use Runtime, Restart session and run all, and fix the first error."
    )


def test_has_a_chart(executed):
    nb, error = executed
    if error:
        pytest.skip("The notebook does not run yet; see test_notebook_runs.")
    charts = [o for c in nb.cells if c.cell_type == "code"
              for o in c.get("outputs", []) if "image/png" in o.get("data", {})]
    assert charts, "The notebook should draw at least one chart (end the chart cell with plt.show())."


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
