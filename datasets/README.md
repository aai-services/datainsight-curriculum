# Teaching datasets

These files are used in lessons and practice exercises. They are rebuilt from their public sources by [`scripts/build_teaching_data.py`](../scripts/build_teaching_data.py).

## Clean datasets

| File | Contents | Source and license |
|---|---|---|
| `penguins.csv` | Measurements of 344 penguins of three species on three islands in Antarctica, 2007 to 2009 | Palmer Penguins (Horst, Hill and Gorman, 2020), from data collected by Dr. Kristen Gorman and Palmer Station LTER. CC0 |
| `life_expectancy.csv` | Period life expectancy at birth, by country and year, 2000 to 2022 | Our World in Data, based on UN World Population Prospects and other sources. CC BY 4.0 |
| `gdp_per_capita.csv` | GDP per person, purchasing power parity, constant international dollars, 2000 to 2022 | Our World in Data, based on World Bank data. CC BY 4.0 |
| `population.csv` | Population by country and year, 2000 to 2022 | Our World in Data, based on HYDE, Gapminder, and UN World Population Prospects. CC BY 4.0 |
| `regions.csv` | Continent for each country | Our World in Data region classification. CC BY 4.0 |
| `countries.csv` | The four country files above, joined by country and year | As above |

Countries only: regional and income-group aggregates are removed. The World Bank does not publish GDP for every country, so `gdp_per_capita.csv` covers fewer countries than the other files; that gap is used in the joining lesson.

## Deliberately damaged datasets

These are copies of the clean data with problems added on purpose, for cleaning practice. **Do not use them for real analysis.**

`messy_countries.csv` (used in lesson 1.3): the years 2010, 2015 and 2020 from `countries.csv`, with:

1. Population stored as text with thousands separators
2. Missing GDP values written as `..` or `n/a`, and missing life expectancy written as `-1`
3. Region names with inconsistent capitals and trailing spaces
4. Twelve exact duplicate rows
5. One impossible life expectancy (Kenya, 2015: an extra zero)

`messy_penguins.csv` (used in practice 1.3): `penguins.csv` with:

1. Species names in inconsistent capitals, some with surrounding spaces
2. Body mass stored as text with a unit (`3750 g`), and missing values written as `.`
3. Some sex values abbreviated to `M` and `F`
4. Three impossible flipper lengths (0, 9999, and a negative value)
5. Eight exact duplicate rows

## Citation

Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version 0.1.0. https://allisonhorst.github.io/palmerpenguins/

Our World in Data, https://ourworldindata.org, CC BY 4.0.
