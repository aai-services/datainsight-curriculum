"""Shared helpers for the project checks."""
import re
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = ROOT / "project.ipynb"


def load():
    return nbformat.read(NOTEBOOK, as_version=4)


def sections(nb):
    """Map each '## Section' heading to the text that follows it, up to the next heading."""
    found, current = {}, None
    for cell in nb.cells:
        lines = cell.source.strip().splitlines()
        heading = re.match(r"^##\s+(.+?)\s*$", lines[0]) if cell.cell_type == "markdown" and lines else None
        if heading:
            current = heading.group(1)
            found[current] = ["\n".join(lines[1:])]
        elif current:
            found[current].append(cell.source)
    return {k: "\n".join(v) for k, v in found.items()}


def markdown_text(nb, section):
    """Only the markdown (not code) under a section heading."""
    found, current = [], None
    for cell in nb.cells:
        lines = cell.source.strip().splitlines()
        if cell.cell_type == "markdown" and lines and lines[0].startswith("## "):
            current = lines[0][3:].strip()
            if current == section:
                found.append("\n".join(lines[1:]))
            continue
        if current == section and cell.cell_type == "markdown":
            found.append(cell.source)
    return "\n".join(found)


def word_count(markdown):
    text = re.sub(r"`[^`]*`|\[([^\]]*)\]\([^)]*\)|[#*_>|-]", r" \1 ", markdown)
    return len(re.findall(r"[A-Za-z0-9\u00C0-\uFFFF']+", text))


def charts(executed_nb):
    return sum(1 for c in executed_nb.cells if c.cell_type == "code"
               for o in c.get("outputs", []) if "image/png" in o.get("data", {}))
