# Checks for practice 1.6. They run after your notebook, in the same session.
import re as _re

import numpy as _np
import pandas as _pd

_pp = _pd.read_csv(DATA + "penguins.csv")
_values = _np.array([2.0, 4.0, 4.0, 5.0, 7.0, 9.0, 10.0, 12.0])


def _bootstrap_ok():
    a = _np.asarray(bootstrap_means(_values, 4000, 3))
    b = _np.asarray(bootstrap_means(_values, 4000, 3))
    expected_se = _values.std() / _np.sqrt(len(_values))
    return (len(a) == 4000 and _np.array_equal(a, b)
            and abs(a.mean() - _values.mean()) < 0.2
            and 0.8 * expected_se < a.std() < 1.2 * expected_se)


check("Exercise 1: bootstrap_means", _bootstrap_ok,
      "Return n_boot means of resamples the same size as values, drawn with replacement, "
      "using np.random.default_rng(seed) inside the function.")
check("Exercise 2: ci_95",
      lambda: _np.allclose(ci_95(_np.arange(1001.0)), _np.percentile(_np.arange(1001.0), [2.5, 97.5])),
      "Return the 2.5th and 97.5th percentiles, for example with np.percentile.")

_rng = _np.random.default_rng(12345)


def _ref_ci(x):
    boots = _rng.choice(x, size=(20000, len(x)), replace=True).mean(axis=1)
    return _np.percentile(boots, [2.5, 97.5])


_chin = _pp.loc[_pp["species"] == "Chinstrap", "bill_length_mm"].dropna().to_numpy()
_ref = _ref_ci(_chin)
check("Exercise 3: ci_chinstrap_bill",
      lambda: abs(ci_chinstrap_bill[0] - _ref[0]) < 0.3 and abs(ci_chinstrap_bill[1] - _ref[1]) < 0.3,
      "Bootstrap the mean bill length of Chinstrap penguins (missing values removed), then take ci_95.")

_g = _pp.loc[_pp["species"] == "Gentoo", "body_mass_g"].dropna().to_numpy()
_c = _pp.loc[_pp["species"] == "Chinstrap", "body_mass_g"].dropna().to_numpy()
_diffs = (_rng.choice(_g, size=(20000, len(_g))).mean(axis=1) - _rng.choice(_c, size=(20000, len(_c))).mean(axis=1))
_ref_d = _np.percentile(_diffs, [2.5, 97.5])
check("Exercise 4: diff", lambda: abs(diff - (_g.mean() - _c.mean())) < 1e-6,
      "Gentoo mean minus Chinstrap mean body mass, with missing values removed.")
check("Exercise 4: diff_ci", lambda: abs(diff_ci[0] - _ref_d[0]) < 25 and abs(diff_ci[1] - _ref_d[1]) < 25,
      "Subtract the Chinstrap bootstrap means from the Gentoo bootstrap means, then take ci_95.")
check("Exercise 5: correct_statement", lambda: str(correct_statement).strip().upper() == "B",
      "The interval is random; the true mean is fixed. Reread 'What the interval means' in lesson 1.6.")
check("Exercise 6: report",
      lambda: len(str(report).split()) >= 25 and len(_re.findall(r"\d[\d,.]*", str(report))) >= 2,
      "Write at least 25 words, including the estimate and the interval as numbers.")
