"""One-line office joke for the make.fun "Make the AI Judge Laugh" bounty.

Stdlib only. Writes exactly one line of text (no trailing newline) to
/output/entry.txt, deterministically.
"""

import os

JOKE = "The office plant has outlasted three managers, two restructures, and one merger \u2014 yesterday HR asked it to onboard the new hire."

assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
assert JOKE.strip(), "entry must not be only whitespace"
assert "\n" not in JOKE and "\r" not in JOKE, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
