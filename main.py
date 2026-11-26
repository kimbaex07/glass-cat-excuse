"""Five Seconds to Explain the Glass — make.fun entry.

Writes the one sentence a house cat would say in its own defence in the
five seconds after sweeping a glass off the table. Pure Python stdlib,
deterministic, no network. The line is written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

# The cat's defence, authored for this entry. One sentence, 1-200 chars,
# in the cat's own voice. No apology, no confession: the glass was a
# non-paying tenant, and gravity was only the courier.
LINE = "That glass had been staring at me all morning and never paid a cent of rent, so I served it an eviction notice \u2014 gravity was just the courier."


def main():
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(
            "entry line must be 1-200 characters, got %d" % len(LINE)
        )
    if LINE != LINE.strip() or "\n" in LINE:
        raise SystemExit("entry line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
