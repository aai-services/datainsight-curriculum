# Curriculum Map

Status: draft for review. Last updated September 2026. First cohort on this structure: January 2027.

## Program structure

The program has two parts. Each ends with its own certificate, so every fellow who finishes a part leaves with a credential.

| Part | Length | Who | Certificate |
|---|---|---|---|
| Core: Applied Data Analysis with AI | 26 weeks | Every fellow | Core Certificate |
| Advanced: one pathway | 26 weeks | Optional; open to fellows who complete the Core | Advanced Certificate in the chosen pathway |

Advanced pathways:

- **Machine Learning and AI Applications**: building, evaluating, and deploying models, including applications of large language models.
- **Analytics for Decisions**: experiments, causal reasoning, forecasting, and communicating results to decision-makers.

## What fellows learn

The program trains the skills that remain with the analyst when AI tools write much of the code:

1. **Framing**: turning a vague problem into a precise, answerable question.
2. **Data judgment**: knowing where data came from, what is missing or biased, and what it cannot answer.
3. **Statistical reasoning**: quantifying uncertainty, and separating association from causation.
4. **Verification**: checking code and results, whether written by a person or an AI tool.
5. **Communication**: honest charts and clear recommendations for a real audience.
6. **Working code literacy**: enough Python and SQL to read, question, and fix code.

## Time commitment and weekly rhythm

Core work is 10 to 12 hours a week. Optional extras (drill platforms, further reading) are listed in each module for fellows who want more.

| Day | Activity | Time |
|---|---|---|
| Monday | Module opens: concept notebook and worked example | about 4 h across the week |
| During the week | Practice exercises with automatic checks | about 3 h |
| During the week | Mini-project or project work | 3 to 4 h |
| Midweek | Pod check-in with mentor (30 minutes, live or written) | 0.5 h |
| Friday | Submission and a two-question reflection | 0.5 h |
| Monthly | Live session or demo day | 1 h |

## How AI is used

AI use changes by stage. Full rules are in the [AI-use policy](policies/ai-use.md).

| Stage | AI mode |
|---|---|
| Core Stages 0 and 1 | Tutor only: explanations, hints, and quizzes. No AI-written code in graded work. |
| Core Stage 2 | Pair programmer, with an AI-use log for each project. |
| Core Stage 3 and Advanced | Full tool, with an AI-use log. Graded on judgment and results. |

## Every module has the same parts

1. Concept notebook (runs in Google Colab; also downloadable)
2. Worked example
3. Practice exercises with automatic checks
4. AI tutor card: prompts that make an AI tool teach step by step instead of giving answers
5. Mini-project or project brief, assessed with the [project rubric](rubrics/project-rubric.md)
6. Two-question reflection

---

## Core: Applied Data Analysis with AI (weeks 1 to 26)

### Stage 0: Onboarding sprint (weeks 1 to 2)

| Week | Module | Content |
|---|---|---|
| 1 | 0.1 Tools and ways of working | GitHub account; Colab; Git basics (commit, push, pull request); Markdown; keeping keys and personal data out of repositories; the AI-use policy |
| 2 | 0.2 First data story | One small public dataset about the fellow's own community; one chart and about 300 words; submitted as a pull request and published on the site |

Milestone: fellows who complete Stage 0 are placed in a pod.

### Stage 1: Foundations (weeks 3 to 10)

| Week | Module or project | Content |
|---|---|---|
| 3 | 1.1 Python essentials | Values and types, lists and dictionaries, conditions, loops, functions |
| 4 | 1.2 Tables with pandas | Loading data, selecting, filtering, sorting, new columns |
| 5 | 1.3 Cleaning data | Missing values, types, duplicates, text and dates; recording every cleaning decision |
| 6 | 1.4 Combining and reshaping | Grouping and aggregation, joins, wide and long formats; checking row counts after every join |
| 7 | Project 1: Clean and describe | Take a messy dataset from the fellow's country, clean it, document each decision, and describe what it contains |
| 8 | 1.5 Describing data | Distributions, center and spread, outliers, comparing groups visually |
| 9 | 1.6 Uncertainty by simulation | Samples and populations, sampling variability, bootstrap confidence intervals |
| 10 | Project 2: Compare two groups | A comparison that reports the size of a difference and its uncertainty, not only whether one exists |

Milestone: Foundations badge.

### Stage 2: Analysis (weeks 11 to 18)

| Week | Module or project | Content |
|---|---|---|
| 11 | 2.1 SQL for analysis | SELECT, WHERE, GROUP BY, JOIN, using DuckDB or SQLite from Python |
| 12 | 2.2 Visualization that tells the truth | Choosing chart types, scales and baselines, recognizing misleading charts |
| 13 | 2.3 Exploratory workflow and provenance | Documenting sources, collection methods, known biases, and limits of the data |
| 14 | Project 3: Explore and explain | An exploratory analysis of local data with a clear question and an honest account of limitations |
| 15 | 2.4 Relationships | Correlation, simple linear regression, confounding, why association is not causation |
| 16 | 2.5 Verifying analysis | Sanity checks, simple tests, reproducibility, reviewing AI-written code |
| 17 | Project 4: Catch the model | Review an AI-generated analysis containing planted errors (for example data leakage, a wrong join, a misleading chart, an overclaimed result); find, explain, and fix them |
| 18 | Revisions and capstone proposal | Revise earlier projects; submit a one-page capstone proposal: question, data, audience |

Milestone: Analysis badge.

### Stage 3: Capstone (weeks 19 to 26)

| Week | Activity |
|---|---|
| 19 | Proposal approved by mentor; data access confirmed |
| 20 to 21 | Data preparation and first analysis |
| 22 | Midpoint peer review |
| 23 to 24 | Analysis, verification, and revision |
| 25 | Deliverables: repository, one-page decision memo for the named audience, 5-minute recorded walkthrough |
| 26 | Demo day; final revisions |

Capstones use local data and name a real audience. Partnering with a nonprofit or public body is encouraged but not required.

Milestone: Core Certificate.

---

## Advanced (weeks 27 to 52, optional)

Fellows who complete the Core can continue into one pathway. Both pathways begin with a shared modeling block.

### Shared block: Modeling foundations (weeks 27 to 32)

| Week | Module or project | Content |
|---|---|---|
| 27 | A.1 Prediction versus explanation | What a model is for; baselines; train and test splits |
| 28 | A.2 Model evaluation | Cross-validation, choosing metrics, class imbalance |
| 29 | A.3 Leakage and honest evaluation | How evaluation goes wrong and how to detect it |
| 30 | A.4 First models | Logistic regression and decision trees with scikit-learn |
| 31 | A.5 Fairness and error analysis | Who the model fails; subgroup performance |
| 32 | Project 5: An honest model | A model with a baseline, sound validation, error analysis, and a clear statement of limits |

### Pathway A: Machine Learning and AI Applications (weeks 33 to 44)

| Week | Module or project | Content |
|---|---|---|
| 33 | A1.1 Tree ensembles and feature engineering | Random forests, gradient boosting |
| 34 | A1.2 Unsupervised learning | Clustering and dimensionality reduction, and how to judge the results |
| 35 to 36 | Project 6: Applied prediction | End-to-end model on local data |
| 37 | A1.3 Neural networks | Core ideas and a small network |
| 38 | A1.4 Working with language models | Calling a model from code, structured outputs, prompt design |
| 39 | A1.5 Evaluating language model outputs | Test sets for model outputs, failure modes, cost and privacy |
| 40 to 41 | Project 7: A language model application | A small tool with an evaluation showing when it works and when it fails |
| 42 | A1.6 Responsible deployment | Monitoring, documentation, model cards |
| 43 to 44 | Project 8: Model review | Audit and improve an existing model or AI tool |

### Pathway B: Analytics for Decisions (weeks 33 to 44)

| Week | Module or project | Content |
|---|---|---|
| 33 | B1.1 Experiments | Randomization, A/B tests, sample size |
| 34 | B1.2 Causal thinking | Causal diagrams, confounding, when observational data can and cannot answer a causal question |
| 35 to 36 | Project 6: Evaluate a program | Assess the effect of a real program or policy, stating assumptions openly |
| 37 | B1.3 Time series | Trend, seasonality, decomposition |
| 38 | B1.4 Forecasting | Simple forecasting methods, evaluating forecasts, communicating forecast uncertainty |
| 39 to 40 | Project 7: Forecast for a decision | A forecast with honest uncertainty for a named decision-maker |
| 41 | B1.5 Dashboards | Building a dashboard people actually use |
| 42 | B1.6 Writing for decision-makers | Memos, briefings, presenting uncertainty |
| 43 to 44 | Project 8: Decision brief | A dashboard and memo for a real organization |

### Advanced capstone (weeks 45 to 52)

Same format as the Core capstone, with a partner organization expected. Possible partners include nonprofits, local agencies, and community project platforms such as Omdena local chapters.

Milestone: Advanced Certificate.

---

## Totals

- Core: 4 projects and 1 capstone.
- Core plus Advanced: 8 projects and 2 capstones.

## Completion and progress

- A project passes when it meets the rubric standard on every criterion, allowing one revision.
- Fellows are expected to submit at least 80 percent of weekly work.
- Missing two consecutive weeks triggers a check-in from the pod mentor.
- Fellows who fall too far behind can pause and rejoin the next cohort at the start of their current stage.

## Tools

All tools are free: Python, Google Colab, GitHub and GitHub Classroom, pandas, DuckDB or SQLite, matplotlib and seaborn, statsmodels, scikit-learn. Language model modules will use a free tier or small open models; the specific service will be confirmed when those modules are built.

## Data

Worked examples use openly licensed datasets. For projects, fellows choose data from their own country or community, for example from national statistics offices, the World Bank, the WHO, Our World in Data, or the Humanitarian Data Exchange. Every project records the source and license of its data.
