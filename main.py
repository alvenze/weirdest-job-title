"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes exactly one job title to /output/entry.txt and nothing else.
Gate: UTF-8 text, 1 to 60 characters, not only whitespace, one line.
"""

import os
import sys

LINE = "Certified Interpreter for Dogs Judging Their Owners"


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 60):
        print(f"gate: line is {len(text)} chars, must be 1-60", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or "\r" in text:
        print("gate: line must be a single line with no padding", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: line must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
