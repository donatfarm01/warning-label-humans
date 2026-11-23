"""Warning Label for Humans — one-line entry writer.

Writes the single-line safety warning label to /output/entry.txt, exactly
as checked: one line, 1 to 160 characters, no trailing newline.
"""

import os

ENTRY = "CAUTION: The hazard is not the machine. This human presses every button marked DO NOT PRESS, then blames the machine."


def main():
    assert 1 <= len(ENTRY) <= 160, "entry must be 1 to 160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back does not match the checked line"


if __name__ == "__main__":
    main()
