# Checks for practice 1.2. They run after your notebook, in the same session.
import numpy as _np
import pandas as _pd

_p = _pd.read_csv(DATA + "penguins.csv")

check("Exercise 1: size", lambda: (n_rows, n_cols) == _p.shape,
      "Use the .shape of the table.")
check("Exercise 2: gentoo",
      lambda: isinstance(gentoo, _pd.DataFrame) and len(gentoo) == (_p["species"] == "Gentoo").sum()
      and set(gentoo["species"]) == {"Gentoo"} and list(gentoo.columns)[:8] == list(_p.columns),
      "Keep all columns and only the rows where species is 'Gentoo'.")
check("Exercise 3: heavy_count", lambda: heavy_count == (_p["body_mass_g"] > 5000).sum(),
      "Count penguins with body_mass_g greater than 5000.")
check("Exercise 4: bill_ratio",
      lambda: _np.allclose(penguins["bill_ratio"], _p["bill_length_mm"] / _p["bill_depth_mm"], equal_nan=True),
      "Add penguins['bill_ratio'] = bill length divided by bill depth.")
check("Exercise 5: top5",
      lambda: list(top5.columns) == ["species", "island", "body_mass_g"]
      and list(top5["body_mass_g"]) == list(_p["body_mass_g"].sort_values(ascending=False).head(5)),
      "Sort by body_mass_g from heaviest, keep five rows and the three named columns.")
check("Exercise 6: dream_counts",
      lambda: dict(dream_counts) == dict(_p.loc[_p["island"] == "Dream", "species"].value_counts()),
      "Filter to island == 'Dream' first, then count species.")
check("Exercise 7: observation", lambda: len(str(observation).split()) >= 15 and "..." not in str(observation),
      "Write at least 15 words in your own words.")
