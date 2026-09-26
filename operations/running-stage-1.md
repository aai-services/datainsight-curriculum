# Running Stage 1 (Program Director checklist)

## Before Stage 1 starts

Publish three more template repositories in the fellows' organization, the same way as for Stage 0 (see [Running Stage 0](running-stage-0.md), step 3):

```bash
for t in stage-1-practice stage-1-project-1 stage-1-project-2; do
  cp -R datainsight-curriculum/templates/$t $t
  cd $t
  git init -b main
  git add -A
  git commit -m "Initial template"
  git remote add origin git@github.com:datainsight-fellows/$t.git
  git push -u origin main
  cd ..
done
```

Tick **Template repository** in each repository's Settings, then create three individual, public Classroom assignments:

| Assignment | Template | Opens | Deadline |
|---|---|---|---|
| Stage 1: Practice | `stage-1-practice` | Week 3 | End of week 9 (each module is due at the end of its own week) |
| Project 1: Clean and describe | `stage-1-project-1` | Week 7 | End of week 7 |
| Project 2: Compare two groups | `stage-1-project-2` | Week 10 | End of week 10 |

The practice repository holds all six practice notebooks, so fellows accept it once.

## Every module week

- **Monday:** announce the module with its lesson link.
- **Office hour:** go through the parts of the lesson that the weekly check-ins flagged.
- **Friday:** skim the Actions results for that week's practice check, for example with the Classroom dashboard, and message fellows whose check is still failing after the weekend.

## Project weeks (7 and 10)

- **Friday:** projects due. Post peer review assignments; the peer groups from Stage 0 continue, so the same table can be reused or regenerated with `scripts/assign_peer_reviews.py`.
- **Two days later:** peer reviews due.
- **You review:** every project where the two reviews disagree on a criterion, plus a random sample of about one in five others. To draw the sample from a file of usernames:

  ```bash
  python -c "import random; names = open('usernames.txt').read().split(); print(sorted(random.sample(names, max(1, len(names) // 5))))"
  ```

- **Following week:** one revision allowed; re-review only the criteria that were "Not yet".

## Rotating peer facilitators

Rotate the facilitator in each peer group every four weeks (weeks 3, 7, and 11). The facilitator starts the weekly check-in thread and flags anyone who goes quiet.

## Updating the teaching datasets

The datasets in `datasets/` are rebuilt from their sources with:

```bash
python scripts/build_teaching_data.py
```

Rebuilding changes the numbers slightly whenever the sources update. Do it between cohorts, not during one, and rerun the lessons and practice checks afterwards.
