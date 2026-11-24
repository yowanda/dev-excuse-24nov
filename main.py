#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production, to <output>/entry.txt. Deterministic, stdlib only, no network.
"""

import os

EXCUSE = "I didn't break production \u2014 I just promoted the staging bug to a much bigger audience."


def _validate_excuse(text: str) -> None:
    if not text or len(text) > 200:
        raise ValueError("excuse must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def main() -> None:
    _validate_excuse(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(EXCUSE.encode("utf-8"))


if __name__ == "__main__":
    main()
