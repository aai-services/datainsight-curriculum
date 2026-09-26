# Runs after the notebook, in the same session.
import pandas as _pd

check("clean data written", lambda: _pd.read_csv(CLEAN_FILE).shape[0] > 0,
      "The notebook should save the cleaned table to data/clean/clean.csv.")
check("raw data kept", lambda: isinstance(raw, _pd.DataFrame) and len(raw) > 0,
      "Load the raw file into `raw` and clean a copy.")
