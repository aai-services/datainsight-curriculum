#!/usr/bin/env python3
"""Draw the Data Insight brand images used in notebook headers and footers.

Writes PNG files to assets/brand/. Run it once, then commit the images:

    python scripts/build_brand_assets.py

The typeface is Public Sans (SIL Open Font License), downloaded on first run
from the U.S. Web Design System repository. If it cannot be downloaded, a
system sans-serif is used instead.
"""
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "brand"
FONT_DIR = Path.home() / ".cache" / "datainsight-fonts"
FONT_URL = "https://raw.githubusercontent.com/uswds/public-sans/develop/fonts/ttf/PublicSans-{}.ttf"

NAVY = "#14213D"
WHITE = "#FFFFFF"
MUTED = "#A9B6C8"
TOPICS = ["#1B998B", "#7B4B94", "#E0A030", "#4F9FDF", "#C8455A"]   # same palette as the website

STAGES = {
    "stage-0": "Stage 0 \u00b7 Onboarding",
    "stage-1": "Stage 1 \u00b7 Foundations",
    "stage-2": "Stage 2 \u00b7 Analysis",
    "stage-3": "Stage 3 \u00b7 Capstone",
}


def font(weight):
    """Return FontProperties for Public Sans, downloading it if needed."""
    path = FONT_DIR / f"PublicSans-{weight}.ttf"
    if not path.exists():
        try:
            FONT_DIR.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(FONT_URL.format(weight), path)
        except OSError:
            return font_manager.FontProperties(family="sans-serif", weight=weight.lower())
    return font_manager.FontProperties(fname=str(path))


def dot_field(ax, x0, x1, y0, y1, seed=7):
    """Columns of small dots, echoing the projects chart on the website."""
    rng = np.random.default_rng(seed)
    cols = 30
    xs = np.linspace(x0, x1, cols)
    # a rise to a peak and a long tail, like a cohort publishing projects
    base = 9 * np.exp(-((np.arange(cols) - 11) / 5.5) ** 2) + 1.5
    heights = np.clip(np.round(base + rng.normal(0, 0.9, cols)), 1, 10).astype(int)
    step = (y1 - y0) / 10
    for x, h in zip(xs, heights):
        for k in range(h):
            ax.scatter(x, y0 + k * step, s=34, color=TOPICS[rng.integers(len(TOPICS))],
                       linewidths=0, alpha=0.95)


def banner(label, path):
    fig = plt.figure(figsize=(16, 3.2), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 3.2)
    ax.axis("off")
    fig.patch.set_facecolor(NAVY)
    ax.text(0.8, 1.72, "Data Insight", color=WHITE, fontproperties=font("Bold"), fontsize=52, va="bottom")
    ax.text(0.83, 1.2, "Open data science curriculum", color=MUTED, fontproperties=font("Regular"),
            fontsize=20, va="center")
    ax.plot([0.83, 6.2], [0.78, 0.78], color=TOPICS[0], linewidth=3, solid_capstyle="butt")
    ax.text(0.83, 0.42, label, color=WHITE, fontproperties=font("Regular"), fontsize=19, va="center")
    dot_field(ax, 10.2, 15.2, 0.55, 2.75)
    fig.savefig(path, facecolor=NAVY)
    plt.close(fig)


def mark(path):
    """Small square mark for footers."""
    fig = plt.figure(figsize=(1, 1), dpi=128)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 32)
    ax.set_ylim(0, 32)
    ax.axis("off")
    ax.add_patch(matplotlib.patches.FancyBboxPatch((0, 0), 32, 32, boxstyle="round,pad=0,rounding_size=6",
                                                   facecolor=NAVY, edgecolor="none"))
    for (x, y), c in zip([(9, 10), (16, 17), (23, 24)], [TOPICS[0], TOPICS[2], TOPICS[3]]):
        ax.add_patch(matplotlib.patches.Circle((x, y), 3.2, color=c))
    fig.savefig(path, transparent=True)
    plt.close(fig)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for key, label in STAGES.items():
        banner(label, OUT / f"banner-{key}.png")
    mark(OUT / "mark.png")
    for p in sorted(OUT.glob("*.png")):
        print(f"{p.relative_to(ROOT)}  {p.stat().st_size / 1e3:.0f} kB")


if __name__ == "__main__":
    main()
