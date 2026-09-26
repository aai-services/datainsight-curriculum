"""Run a practice notebook, then run its checks inside the same Python session."""
import json
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parent.parent
MARKER = "@@CHECK-RESULTS@@"

RUNNER = '''
import json as _json
_check_results = []

def check(name, test, hint):
    try:
        passed = bool(test())
    except Exception as err:
        passed = False
        if isinstance(err, NameError) or "ellipsis" in str(err):
            hint = f"{hint} (not answered yet)"
        else:
            hint = f"{hint} (checking raised {type(err).__name__}: {err})"
    _check_results.append({"name": name, "passed": passed, "hint": hint})

exec(open(r"CHECKS_PATH", encoding="utf-8").read())
print("MARKER" + _json.dumps(_check_results))
'''


def run(notebook, checks):
    """Return (results, error). error is set when the notebook itself fails."""
    _, results, error = run_full(notebook, checks)
    return results, error


def run_full(notebook, checks):
    """Return (executed notebook, results, error)."""
    nb = nbformat.read(ROOT / notebook, as_version=4)
    n_cells = len(nb.cells)
    runner = RUNNER.replace("CHECKS_PATH", str(ROOT / "tests" / checks)).replace("MARKER", MARKER)
    nb.cells.append(nbformat.v4.new_code_cell(runner))
    client = NotebookClient(nb, timeout=600, kernel_name="python3",
                            resources={"metadata": {"path": str(ROOT)}})
    try:
        client.execute()
    except CellExecutionError as err:
        failed = next((i for i, c in enumerate(nb.cells)
                       if any(o.get("output_type") == "error" for o in c.get("outputs", []))), None)
        if failed is not None and failed < n_cells:
            first_line = nb.cells[failed].source.strip().splitlines()[0][:60]
            return nb, None, f"the cell starting `{first_line}`: {err.ename}: {err.evalue}"
        raise
    for output in nb.cells[-1].get("outputs", []):
        text = output.get("text", "")
        if MARKER in text:
            return nb, json.loads(text.split(MARKER, 1)[1]), None
    raise RuntimeError("The checks did not report any results.")
