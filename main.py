#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt (or $OUTPUT_PATH):
"A" for coffee. A is the first letter and the top grade - the first,
boldest choice - and coffee is the bolder, more vivid drink: dark,
hot, and alive, where tea is calm. A single letter, nothing else.
"""

import os

LETTER = "A"  # coffee


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Exactly one character, no trailing newline: the gate is 1 to 1 chars.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()

# Notes on the choice: the gate allows exactly one character, so the
# entry is the letter alone. "A" stands for coffee - the first letter,
# the top mark, and the drink that hits first and hardest.
