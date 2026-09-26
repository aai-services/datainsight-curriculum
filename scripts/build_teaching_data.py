#!/usr/bin/env python3
"""Build the teaching datasets in datasets/ from their public sources.

Sources (downloaded when this script runs):
- Palmer Penguins, Horst, Hill and Gorman (2020), CC0:
  https://github.com/allisonhorst/palmerpenguins
- Our World in Data (CC BY 4.0), which credits the original sources:
  life expectancy (UN World Population Prospects and other sources),
  GDP per capita, PPP (World Bank), population (OWID compilation of HYDE,
  Gapminder, and UN WPP), and the OWID continent classification.

The "messy" files are deliberately damaged copies of the clean data, made for
cleaning exercises. Every change is listed in datasets/README.md. The damage is
seeded, so running this script again produces identical files.

Usage:
    python scripts/build_teaching_data.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent / "datasets"
PENGUINS = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
OWID = "https://ourworldindata.org/grapher/{}.csv?v=1&csvType=full&useColumnShortNames=true"
YEARS = range(2000, 2023)


def owid(slug, column, new_name):
    df = pd.read_csv(OWID.format(slug), storage_options={"User-Agent": "Mozilla/5.0"})
    # Keep countries only: aggregates have no code, or a code that is not three letters.
    df = df[df["code"].fillna("").str.fullmatch(r"[A-Z]{3}")]
    df = df[df["year"].isin(YEARS)]
    return df.rename(columns={"entity": "country", column: new_name})


def build_countries():
    life = owid("life-expectancy", "life_expectancy_0", "life_expectancy")
    gdp = owid("gdp-per-capita-worldbank", "ny_gdp_pcap_pp_kd", "gdp_per_capita")
    pop = owid("population", "population_historical", "population")

    regions = pd.read_csv(OWID.format("continents-according-to-our-world-in-data"),
                          storage_options={"User-Agent": "Mozilla/5.0"})
    regions = (regions[regions["code"].fillna("").str.fullmatch(r"[A-Z]{3}")]
               .rename(columns={"entity": "country", "owid_region": "region"})
               [["country", "code", "region"]]
               .drop_duplicates("code"))
    life = life[["country", "code", "year", "life_expectancy"]].round({"life_expectancy": 2})
    gdp = gdp[["country", "code", "year", "gdp_per_capita"]].round({"gdp_per_capita": 0})
    pop = pop[["country", "code", "year", "population"]]

    life.to_csv(OUT / "life_expectancy.csv", index=False)
    gdp.to_csv(OUT / "gdp_per_capita.csv", index=False)
    pop.to_csv(OUT / "population.csv", index=False)
    regions.to_csv(OUT / "regions.csv", index=False)

    countries = (life.merge(gdp, on=["country", "code", "year"], how="outer")
                     .merge(pop, on=["country", "code", "year"], how="left")
                     .merge(regions[["code", "region"]], on="code", how="left")
                     .sort_values(["country", "year"]))
    countries = countries[["country", "code", "region", "year",
                           "life_expectancy", "gdp_per_capita", "population"]]
    countries.to_csv(OUT / "countries.csv", index=False)
    return countries


def build_messy_countries(countries, rng):
    """A damaged extract used in the 1.3 lesson."""
    df = countries[countries["year"].isin([2010, 2015, 2020])].copy().reset_index(drop=True)
    df = df.dropna(subset=["region"])
    df["region"] = df["region"].astype(object)
    # 1. Population stored as text with thousands separators.
    df["population"] = df["population"].map(lambda v: "" if pd.isna(v) else f"{int(v):,}")
    # 2. Missing values coded in three different ways.
    df["gdp_per_capita"] = df["gdp_per_capita"].astype(object)
    idx = rng.choice(df.index, 40, replace=False)
    df.loc[idx[:15], "gdp_per_capita"] = ".."
    df.loc[idx[15:30], "gdp_per_capita"] = "n/a"
    df.loc[idx[30:], "life_expectancy"] = -1
    # 3. Inconsistent spelling and spacing of region names.
    idx = rng.choice(df.index, 30, replace=False)
    df.loc[idx[:10], "region"] = df.loc[idx[:10], "region"].str.upper()
    df.loc[idx[10:20], "region"] = df.loc[idx[10:20], "region"] + " "
    df.loc[idx[20:], "region"] = df.loc[idx[20:], "region"].str.lower()
    # 4. Exact duplicate rows.
    df = pd.concat([df, df.sample(12, random_state=rng.integers(1e9))], ignore_index=True)
    # 5. An impossible value (a data entry slip: an extra zero).
    kenya = df["country"].eq("Kenya") & df["year"].eq(2015)
    true_value = countries.loc[countries["country"].eq("Kenya") & countries["year"].eq(2015), "life_expectancy"].item()
    df.loc[kenya, "life_expectancy"] = true_value * 10
    df = df.sample(frac=1, random_state=rng.integers(1e9)).reset_index(drop=True)
    df.to_csv(OUT / "messy_countries.csv", index=False)


def build_messy_penguins(penguins, rng):
    """A damaged copy used in the 1.3 practice exercises."""
    df = penguins.copy()
    idx = rng.choice(df.index, 60, replace=False)
    df["species"] = df["species"].astype(object)
    df["sex"] = df["sex"].astype(object)
    df.loc[idx[:20], "species"] = df.loc[idx[:20], "species"].str.upper()
    df.loc[idx[20:40], "species"] = " " + df.loc[idx[20:40], "species"].str.lower() + " "
    df["body_mass_g"] = df["body_mass_g"].map(lambda v: "." if pd.isna(v) else f"{int(v)} g")
    idx = rng.choice(df.index[df["sex"].notna()], 30, replace=False)
    df.loc[idx, "sex"] = df.loc[idx, "sex"].map({"male": "M", "female": "F"})
    idx = rng.choice(df.index[df["flipper_length_mm"].notna()], 3, replace=False)
    df.loc[idx, "flipper_length_mm"] = [0, 9999, -181]
    df = pd.concat([df, df.sample(8, random_state=rng.integers(1e9))], ignore_index=True)
    df = df.sample(frac=1, random_state=rng.integers(1e9)).reset_index(drop=True)
    df.to_csv(OUT / "messy_penguins.csv", index=False)


def main():
    OUT.mkdir(exist_ok=True)
    rng = np.random.default_rng(2027)
    penguins = pd.read_csv(PENGUINS)
    penguins.to_csv(OUT / "penguins.csv", index=False)
    countries = build_countries()
    build_messy_countries(countries, rng)
    build_messy_penguins(penguins, rng)
    for f in sorted(OUT.glob("*.csv")):
        print(f"{f.name:28s} {sum(1 for _ in open(f)) - 1:6d} rows  {f.stat().st_size / 1e3:7.1f} kB")


if __name__ == "__main__":
    main()
