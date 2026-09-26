# Project 2: Compare two groups

Week 10. About 12 hours.

Compare two groups in data from your country or community, estimate the size of the difference, and measure its uncertainty with a bootstrap confidence interval.

## Choosing a comparison

Choose two groups and one numeric measure, for example:

- Rainfall in two decades, at one weather station
- School enrolment rates in rural and urban districts
- Market prices of a staple food in two regions

Each group needs **at least 15 values**; more is better. The data must be public, with a known license and no personal information. You may reuse your Project 1 data if it fits.

## What to submit

Accept the **Project 2** assignment and complete `project.ipynb`:

| Section | What to write |
|---|---|
| Question | Which groups, which measure, and why the difference matters to someone |
| Data | Source link, license, coverage, and how each group is defined |
| Method | The statistic you compare (mean or median, and why) and how you estimate uncertainty |
| Results | The difference (group A minus group B) with a 95% bootstrap confidence interval, and one chart showing both groups' full distributions |
| Interpretation | 150 to 400 words: the difference and its interval in plain language, and what it means for the person who would care |
| Limitations | At least 50 words: how the groups were formed, other explanations for the difference, who is missing |
| Reflection | What was hardest, what you would do next, and how you used AI tools |

## How it is assessed

- **Automatic checks** confirm the project is complete, runs, and reports a difference with an interval.
- **Two peers** review it with the [project rubric](../../rubrics/project-rubric.md). The Program Director reviews a sample and settles disagreements.
- You may revise once after feedback.

## What good looks like

- The size of the difference comes first, then its uncertainty: "about 800 g heavier (95% CI 700 to 900 g)", not only "significantly different".
- The interval is interpreted correctly (see lesson 1.6).
- The Limitations section considers whether something other than group membership could explain the difference.

## AI use

Tutor only. AI tools may explain concepts and error messages, but may not write your code or text.
