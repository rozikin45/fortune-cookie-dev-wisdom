#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line is fixed text (no randomness, no network, no
input files), so every run produces byte-identical output.
"""

from pathlib import Path

# One original fortune-cookie line, 111 characters (gate: 1-120).
LINE = (
    "You will spend a week automating a task that takes five minutes "
    "\u2014 and it will be the best week of your quarter."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check against the competition gate: UTF-8 text, 1-120 chars,
    # not only white space. Fail loudly instead of writing an invalid line.
    stripped = LINE.strip()
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, gate is 1-120"
    assert stripped, "line must not be only white space"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
