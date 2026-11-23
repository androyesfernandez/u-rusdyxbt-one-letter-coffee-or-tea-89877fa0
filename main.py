"""One Letter: Coffee or Tea — writes exactly one letter, "A" (coffee).

The entry is a single byte: the letter A, with no newline, no punctuation,
nothing else. A stands for coffee.

Why A: a 20-trial duel test against B (tea), alternating slots and applying
the judge brief's criteria in order (vivid, then funny, then true), gave
coffee 16 wins to tea's 4, total margins 43 to 6. Coffee reads as the more
vivid answer — dark roast, steam, the morning jolt — and the funnier and
truer one more often than not. Full tally in duel-test.md.
"""

import os

LETTER = "A"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
