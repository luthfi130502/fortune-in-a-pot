#!/usr/bin/env python3
"""Fortune in a Pot — a single-line fortune for the houseplant on the windowsill.

Writes the fortune to /output/entry.txt. Pure Python 3 stdlib.
"""

import os

FORTUNE = (
    "This spring, a stranger will admire you through the glass, "
    "and your keeper will finally water you on purpose."
)


def main() -> None:
    # Gate: UTF-8, 1-120 characters, single line, not only whitespace.
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} chars"
    assert "\n" not in FORTUNE and FORTUNE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
