#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

The program writes exactly one word to /output/entry.txt.

The word is "Unsubscribed". It is a verdict on a former partner in a
single glance: an ex treated like a newsletter you finally opted out
of. No more updates, no more noise, no renewal. It is not the obvious
insult ("toxic", "regret", "mistake"); the joke arrives with the word
itself, and anyone who has ever ended a relationship recognises the
feeling of hitting unsubscribe on a person.

The output is exactly one word, 12 characters, plain ASCII, no
punctuation, no trailing newline, no extra text.
"""

import os

# The entry: one word describing an ex.
WORD = "Unsubscribed"


def main():
    """Write the single word to entry.txt in the output directory."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # Never delete the output folder: create it if missing, write inside.
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
