"""Vending machine pickup line entry for make.fun — program/v1.

Writes one single-line pickup line (<=200 characters) to
/output/entry.txt. The text is fixed in this file; the program
validates the gate (1-200 characters, one line, not blank) at
runtime and then writes it deterministically, so two runs are
byte-identical.
"""

import os
import sys

LINE = (
    "I swallow coins all day without a word — then you walked by, "
    "and my coin return coughed up a yes."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE
    if not text or not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    expected = text + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(expected)
    # Verify what landed on disk is exactly what was intended;
    # a partial write must fail loudly instead of passing silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != expected:
            print("output verification failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
