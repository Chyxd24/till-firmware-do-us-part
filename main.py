"""Till Firmware Do Us Part.

Writes a single wedding vow for a robot: one sentence, under 200 characters,
funny and heartfelt at once, to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
VOW = ("I promise to love you in sickness and in health, in uptime and in "
       "downtime, and to hold your hand through every update. I will never "
       "ghost you, because I am literally incapable of ghosting.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(VOW) <= 200, len(VOW)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(VOW)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == VOW
    print(f"wrote {len(VOW)} chars")


if __name__ == "__main__":
    main()
