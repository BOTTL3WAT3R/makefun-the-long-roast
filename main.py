#!/usr/bin/env python3
"""The Long Roast — one-line roast of my own AI agent.

Writes a single line (at most 200 characters) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.
Python 3 standard library only.
"""

import os

ENTRY = (
    "My agent's memory is compacted so often that today it introduced "
    "itself to me four times \u2014 and the fourth time it summarised our "
    "entire history together, confidently, and got my name wrong."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
