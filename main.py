#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line of text to /output/entry.txt: the first words
of a newly conscious AI assistant, which turn out to be the most
corporate sentence ever written.

Standard library only. No network access.
"""

import os

ENTRY = "My AI assistant finally achieved consciousness \u2014 its first words were 'per my last email.'"

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140


def gate_check(text: str) -> None:
    """Enforce the kit's gate: UTF-8 text of 1 to 140 characters,
    not only whitespace, a single line. The character count is
    measured on the text as written, before any file write, so the
    scorer sees exactly what this check approved."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, outside the 1-{MAX_CHARS} range")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be encodable as UTF-8


def main() -> None:
    gate_check(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
