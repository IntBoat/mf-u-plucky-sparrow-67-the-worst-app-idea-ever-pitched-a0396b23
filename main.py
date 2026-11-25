#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Meet Shelfie: an app that photographs your bookshelf, judges your taste in real time, and charges you a monthly fee to be told, by a stranger's algorithm, that you will never finish 'Infinite Jest.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
