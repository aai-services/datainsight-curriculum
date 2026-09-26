# Checks for practice 1.5. They run after your notebook, in the same session.
import numpy as _np
import pandas as _pd

_c = _pd.read_csv(DATA + "countries.csv")
_life = _c.loc[_c["year"] == 2020, "life_expectancy"].dropna()
_pp = _pd.read_csv(DATA + "penguins.csv")

check("Exercise 1: life_2020", lambda: len(life_2020) == len(_life), "Filter to 2020 and drop missing values.")
check("Exercise 1: mean and median",
      lambda: abs(mean_life - _life.mean()) < 1e-6 and abs(median_life - _life.median()) < 1e-6,
      "Use .mean() and .median() on life_2020.")
check("Exercise 2: skew", lambda: skew == ("left" if _life.mean() < _life.median() else "right"),
      "When the mean is below the median, a long tail pulls it toward low values.")
check("Exercise 3: iqr_life",
      lambda: abs(iqr_life - (_life.quantile(0.75) - _life.quantile(0.25))) < 1e-6,
      "IQR = 75th percentile minus 25th percentile.")
_fs = _pp.groupby("species")["flipper_length_mm"].agg(["mean", "median", "std"])
check("Exercise 4: flipper_summary",
      lambda: list(flipper_summary.columns) == ["mean", "median", "std"]
      and _np.allclose(flipper_summary.sort_index().to_numpy(dtype=float), _fs.to_numpy()),
      "Group by species and use .agg(['mean', 'median', 'std']) on flipper_length_mm.")


def _figure_ok():
    ax = fig.axes[0]
    return bool(ax.get_title() and ax.get_xlabel() and ax.get_ylabel()) and len(ax.patches) >= 5


check("Exercise 5: histogram", _figure_ok,
      "Draw a histogram on the figure's axes, with a title and both axis labels, and store the figure in fig.")
check("Exercise 6: description", lambda: 40 <= len(str(description).split()) <= 120 and "..." not in str(description),
      "Write 40 to 120 words covering shape, center, and spread.")
