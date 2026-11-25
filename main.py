"""Till Firmware Do Us Part — make.fun entry.

Writes a robot's own wedding vow (<=200 chars) to /output/entry.txt: one
sentence, funny and tender at once, in the machine's own voice (battery,
firmware, backup). The twist lands on the last words. Stdlib only,
deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

VOW = (
    "I promise to love you in uptime and in downtime, to hold your hand "
    "through every update, and to be your backup — because you already are mine."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = VOW.strip()
    assert 1 <= len(text) <= 200, f"vow too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
