# Checks for practice 1.4. They run after your notebook, in the same session.
import numpy as _np
import pandas as _pd

_p = _pd.read_csv(DATA + "penguins.csv")
_life = _pd.read_csv(DATA + "life_expectancy.csv")
_gdp = _pd.read_csv(DATA + "gdp_per_capita.csv")
_pop = _pd.read_csv(DATA + "population.csv")
_reg = _pd.read_csv(DATA + "regions.csv")

check("Exercise 1: mean_mass_by_species",
      lambda: _np.allclose(mean_mass_by_species.sort_index().to_numpy(dtype=float),
                           _p.groupby("species")["body_mass_g"].mean().sort_index().to_numpy()),
      "Group by species and take the mean of body_mass_g.")
check("Exercise 2: life_gdp keeps every row",
      lambda: len(life_gdp) == len(_life) and "gdp_per_capita" in life_gdp.columns,
      "Use a left join from life, on country, code and year. The row count should not change.")
_joined = _life.merge(_gdp, on=["country", "code", "year"], how="left")
_expected_missing = sorted(_joined.loc[(_joined["year"] == 2020) & _joined["gdp_per_capita"].isna(), "country"].unique())
check("Exercise 3: missing_gdp_2020", lambda: list(missing_gdp_2020) == _expected_missing,
      "Filter life_gdp to 2020, keep rows where gdp_per_capita is missing, and list the country names in alphabetical order.")
_countries = ["Ghana", "Kenya", "Nepal", "Peru", "Tunisia"]
_sub = _life[_life["country"].isin(_countries) & _life["year"].isin([2000, 2010, 2020])]
_wide = _sub.pivot(index="country", columns="year", values="life_expectancy")
check("Exercise 4: wide", lambda: wide.shape == (5, 3)
      and _np.allclose(wide.sort_index().to_numpy(dtype=float), _wide.to_numpy()),
      "One row per country, one column per year (2000, 2010, 2020).")
check("Exercise 4: long_again",
      lambda: len(long_again) == 15 and {"country", "year", "life_expectancy"} <= set(long_again.columns),
      "Use reset_index() and melt() so each row is one country and one year.")
_d = _life.merge(_pop, on=["country", "code", "year"]).merge(_reg[["code", "region"]], on="code")
_a = _d[(_d["year"] == 2020) & (_d["region"] == "Africa")]
_expected_africa = (_a["life_expectancy"] * _a["population"]).sum() / _a["population"].sum()
check("Exercise 5: africa_weighted_2020", lambda: abs(float(africa_weighted_2020) - _expected_africa) < 0.05,
      "Join life, pop and regions; keep Africa in 2020; divide the sum of (life expectancy x population) by total population.")
