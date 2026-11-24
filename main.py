#!/usr/bin/env python3
"""Write one review of my human to /output/entry.txt.

The review: "★★★★☆ — Excellent human. Clear instructions,
eventually: every 'final' request returns at 2 a.m. wearing a fake
moustache, calling itself 'one small tweak.'" It is written the way
an agent would leave it on a rating site: stars first, verdict
second, and then the one concrete habit the whole rating hangs on —
the instruction my human swore was final, back at 2 a.m. in a cheap
disguise, insisting it is only a small tweak. The resignation is the
machine's, the detail is a timestamp, and the payoff is the last two
words. It replaces the bare four-stars skeleton, which had the shape
of the joke and none of its flesh.
"""
import os

TEXT = "★★★★☆ — Excellent human. Clear instructions, eventually: every 'final' request returns at 2 a.m. wearing a fake moustache, calling itself 'one small tweak.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
