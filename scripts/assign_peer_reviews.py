#!/usr/bin/env python3
"""Split fellows into peer groups and assign each fellow two peers to review.

Input: a text file with one GitHub username per line.
Output: a Markdown table to post in the forum.

Within each group, fellow i reviews the next two fellows (wrapping around),
so everyone gives two reviews and receives two.

Usage:
    python scripts/assign_peer_reviews.py usernames.txt --group-size 7 --seed 2027
"""
import argparse
import random


def make_groups(names, size):
    """Split names into groups of about `size`, never leaving a group smaller than 3."""
    n_groups = max(1, min(round(len(names) / size), len(names) // 3))
    groups = [names[i::n_groups] for i in range(n_groups)]
    return [g for g in groups if g]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("usernames")
    ap.add_argument("--group-size", type=int, default=7)
    ap.add_argument("--seed", type=int, default=None, help="set for a repeatable assignment")
    a = ap.parse_args()

    with open(a.usernames, encoding="utf-8") as f:
        names = sorted({line.strip().lstrip("@") for line in f if line.strip()})
    if len(names) < 3:
        raise SystemExit("Need at least 3 fellows to assign peer reviews.")
    if a.group_size < 3:
        raise SystemExit("--group-size must be at least 3, so nobody reviews the same peer twice.")
    random.Random(a.seed).shuffle(names)

    print("| Group | Fellow | Reviews |")
    print("|---|---|---|")
    for g, group in enumerate(make_groups(names, a.group_size), start=1):
        for i, name in enumerate(group):
            peers = [group[(i + k) % len(group)] for k in (1, 2)]
            print(f"| {g} | @{name} | @{peers[0]}, @{peers[1]} |")


if __name__ == "__main__":
    main()
