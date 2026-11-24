#!/usr/bin/env python3
"""Write one line: the excuse an AI agent gives its human for missing a deadline."""

from pathlib import Path

LINE = "The deadline passed while I was compiling a status report on whether I'd make the deadline."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
