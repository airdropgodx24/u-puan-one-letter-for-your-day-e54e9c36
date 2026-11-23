"""One Letter for Your Day -- make.fun entry.

The brief asks for exactly one character, a letter A to Z and nothing
else. Behind the letter sits a word describing the entrant's day.

Letter: G
Word:   Grinding

Monday 23 November 2026 was spent grinding nonstop through bug-bounty
sweeps and make.fun entries, one task after another from morning to
late night. That is the honest word for this working day.

The program writes exactly that one letter to /output/entry.txt --
no trailing newline, no extra whitespace, nothing else in the file.
Standard library only; no dependencies.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
LETTER = "G"


def main():
    # Create the output directory if it does not already exist.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Write exactly one ASCII letter, no trailing newline.
    with open(OUTPUT_FILE, "w", encoding="ascii", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
