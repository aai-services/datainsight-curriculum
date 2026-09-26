# Checks for practice 1.3. They run after your notebook, in the same session.
import numpy as _np
import pandas as _pd

_raw = _pd.read_csv(DATA + "messy_penguins.csv")
_ref = _pd.read_csv(DATA + "penguins.csv")

check("raw is unchanged", lambda: raw.equals(_raw),
      "Work on clean = raw.copy() and leave raw as it was loaded.")
check("species names", lambda: set(clean["species"].dropna()) == {"Adelie", "Chinstrap", "Gentoo"}
      and clean["species"].notna().all(),
      "Every row should have one of exactly three names: Adelie, Chinstrap, Gentoo.")
check("body mass is numeric", lambda: _pd.api.types.is_numeric_dtype(clean["body_mass_g"]),
      "Convert body_mass_g to numbers: remove the ' g' unit and treat '.' as missing.")
check("body mass values",
      lambda: clean["body_mass_g"].notna().sum() == _ref["body_mass_g"].notna().sum()
      and clean["body_mass_g"].between(2000, 7000).sum() == clean["body_mass_g"].notna().sum(),
      "After cleaning there should be 342 weights, all in grams (between 2,000 and 7,000).")
check("sex values", lambda: set(clean["sex"].dropna()) == {"male", "female"}
      and (clean["sex"] == "male").sum() == (_ref["sex"] == "male").sum(),
      "Use only 'male' and 'female' (and missing). What do 'M' and 'F' stand for?")
check("flipper lengths",
      lambda: not ((clean["flipper_length_mm"] <= 0) | (clean["flipper_length_mm"] > 300)).any()
      and clean["flipper_length_mm"].notna().sum() == _ref["flipper_length_mm"].notna().sum() - 3,
      "Set impossible flipper lengths (at or below 0, or above 300) to missing; do not delete the rows.")
check("no duplicates", lambda: not clean.duplicated().any() and len(clean) == len(_ref),
      "Remove exact duplicate rows. The clean table should have 344 rows.")
check("cleaning log", lambda: isinstance(cleaning_log, list) and len(cleaning_log) >= 5
      and all(len(str(s).split()) >= 4 for s in cleaning_log),
      "Add at least five decisions to cleaning_log, each a short sentence.")
