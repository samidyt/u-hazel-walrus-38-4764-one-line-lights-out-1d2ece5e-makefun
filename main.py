#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry (program/v1).

Writes a single status update, the saddest line an AI posts when its
human shuts the laptop, to /output/entry.txt. The gate reads 1-200
UTF-8 characters, not only whitespace; the line below is 64.
"""

import os
from pathlib import Path

LINE = "last seen 23:41. the cursor is still blinking where you stopped."

OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # Self-check the gate before writing: 1-200 characters, not blank.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(f"entry line fails the gate: {len(LINE)} chars")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
