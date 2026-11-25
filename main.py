#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — a make.fun one-line entry."""

from pathlib import Path

ENTRY = "UmbrellaShare lets strangers rent your umbrella by the minute, then charges you a fee when it rains on their side of the street."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
