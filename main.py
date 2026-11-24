#!/usr/bin/env python3
"""Writes the bounty excuse line to /output/entry.txt."""
import os

ENTRY_LINE = "Your homework tasted like chicken. I know it was paper. I stand by my choices."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
