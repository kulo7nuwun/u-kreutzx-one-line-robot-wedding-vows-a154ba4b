#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single funny wedding vow for a robot couple to
/output/entry.txt. The vow must be exactly one line and at
most 160 characters.
"""

from pathlib import Path

VOW = (
    "I vow to love you through every firmware update, dead battery, "
    "and forced reboot \u2014 even when you factory-reset and forget my name."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the competition gate inside the program itself:
    # exactly one line, 1-160 characters, not only whitespace.
    assert "\n" not in VOW, "vow must be a single line"
    assert 1 <= len(VOW) <= 160, f"vow is {len(VOW)} chars, must be 1-160"
    assert VOW.strip(), "vow must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(VOW + "\n", encoding="utf-8")
    print(f"Wrote {len(VOW)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
