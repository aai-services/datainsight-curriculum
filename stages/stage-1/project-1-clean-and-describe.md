# Project 1: Clean and describe

Week 7. About 12 hours.

Take a messy public dataset about your country or community, clean it, document every decision, and describe what it shows.

## Choosing data

Choose data that is **messy enough to need real cleaning**: numbers stored as text, several ways of writing "missing", inconsistent names, or duplicates. Statistics office downloads and spreadsheets published by agencies are often good choices. The data must be public, with a known license, and contain no personal information. Keep the file under 5 MB.

Avoid the course datasets and anything a peer in your group has already chosen.

## What to submit

Accept the **Project 1** assignment and complete `project.ipynb`:

| Section | What to write |
|---|---|
| Question | What you want to find out, and who would care |
| Data | Source link, license, and what the data covers |
| Cleaning | Code that cleans a copy of the raw data step by step, with a check after each step, and saves the result to `data/clean/clean.csv` |
| Cleaning log | Every decision, one per line, with the reason: at least five |
| Description | At least two charts and 150 to 400 words: shape, center, spread, group differences, surprises, with numbers |
| Limitations | At least 50 words on what the data cannot tell us |
| Reflection | What was hardest, what you would do next, and how you used AI tools |

## How it is assessed

- **Automatic checks** confirm the project is complete and runs.
- **Two peers** review it with the [project rubric](../../rubrics/project-rubric.md). The program lead reviews a sample and settles disagreements.
- You may revise once after feedback.

## What good looks like

- Your raw file is never edited by hand; all cleaning is in code.
- Each cleaning step has a check (`assert`) that would fail if the step went wrong.
- A reader could disagree with a cleaning decision because you explained it.
- The description uses the median and IQR for skewed data, and says what is missing.

## AI use

Tutor only. AI tools may explain error messages or pandas functions, but may not write your code or text.
