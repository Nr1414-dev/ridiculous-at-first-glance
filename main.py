#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — entry program.

Writes one sentence (134 characters) pitching a bizarre startup idea to
/output/entry.txt. The pitch: pressing a voicemail onto vinyl for
grandparents. Stdlib only; no network, no file reads outside this program.
"""
import os
import sys

LINE = (
    "Let us press your voicemail onto vinyl for $50 \u2014 grandparents "
    "pay because a message they can hold beats a grandchild they can't "
    "reach."
)


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}",
              file=sys.stderr)
        return 1
    if text.strip() != text or not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if text.count(".") != 1:
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("ENTRY_OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
