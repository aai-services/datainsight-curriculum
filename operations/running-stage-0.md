# Running Stage 0 (Program Director checklist)

Everything below uses free services.

## Before the cohort (November to December)

### 1. A GitHub organization for fellows' work

Create a free organization, for example `datainsight-fellows`. GitHub Classroom creates one repository per fellow per assignment, which would clutter `aai-services`.

### 2. Make the fellows' repositories public

Choose **public** repositories in each Classroom assignment:

- **Peer review works without extra setup.** Anyone can open an issue on a public repository. With private repositories you would have to add two reviewers to every fellow's repository by hand.
- **Automatic checks stay free.** GitHub Actions minutes are unlimited for public repositories. Free organizations get only a monthly allowance (2,000 minutes when this was written) for private repositories, which a cohort of 80 could exhaust.
- **Fellows build a public portfolio** from their first week.

The trade-off: fellows can see each other's work before the deadline. For Stage 0 this is acceptable, and the AI-use policy and peer review make copying easy to spot.

### 3. Template repositories

Each folder under `templates/` becomes its own template repository in the fellows' organization. From your workspace folder (the one that contains `datainsight-curriculum`):

```bash
for t in stage-0-tools-check stage-0-first-data-story; do
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

Create the two empty public repositories on GitHub first. Then, in each repository's Settings, tick **Template repository**.

### 4. GitHub Classroom

At classroom.github.com, create a classroom linked to the fellows' organization, then two **individual** assignments:

| Assignment | Template | Visibility | Deadline |
|---|---|---|---|
| Stage 0: Tools check | `stage-0-tools-check` | Public | End of week 1 |
| Stage 0: First data story | `stage-0-first-data-story` | Public | End of week 2 |

Copy each assignment's invitation link.

### 5. Forum and forms

- Turn on **Discussions** in the `datainsight-curriculum` repository (Settings, Features). Suggested categories: Announcements, Q&A, Stage 0, Show and tell.
- Create the Tally form for the [weekly check-in](weekly-check-in.md).

### 6. Dry run

Complete both assignments yourself from a second GitHub account, following only the fellow-facing instructions. Fix anything that confused you before January.

## Week 1

- **Monday:** post the tools check invitation link and a welcome message in Announcements.
- **Office hour:** Git, pull requests, and Colab, live.
- **Friday:** tools check due; weekly check-in due.

## Week 2

- **Monday:** post the first data story invitation link.
- **Wednesday:** put the GitHub usernames of everyone who submitted into a text file, one per line, and generate peer groups and review assignments:

  ```bash
  python datainsight-curriculum/scripts/assign_peer_reviews.py usernames.txt --group-size 7 --seed 2027
  ```

  Post the table in the forum. The same groups continue as peer groups in Stage 1.
- **Friday:** story and weekly check-in due; peer reviews due two days after assignment.

## After week 2

- Mark who finished Stage 0 (the four conditions in the Stage 0 README).
- Where two peer reviews disagree, decide.
- Choose the first peer facilitator in each group.
- Admit up to 40 fellows to Stage 1.
