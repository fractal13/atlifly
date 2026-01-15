#!/usr/bin/env python3
"""Random Order - Shuffle and rename PDF files with numbered prefixes.

This tool helps randomize the order of PDF files in a directory by:
1. Cleaning up filenames (removing spaces, special characters)
2. Shuffling the files randomly
3. Renaming them with sequential number prefixes (01-, 02-, etc.)
"""

import os
import re
import random
import sys


def shuffle():
    """Shuffle PDF files in the current directory with numbered prefixes."""
    # First pass: clean up filenames
    for f in os.listdir("."):
        match = re.match("^([0-9]+-)?(.*\\.pdf)", f, re.IGNORECASE)
        if match:
            new_name = f.replace(" ", "-")
            new_name = new_name.replace("'", "_")
            new_name = new_name.replace("(", "_")
            new_name = new_name.replace(")", "_")
            if new_name != f:
                os.rename(f, new_name)

    # Second pass: collect PDF files
    files = []
    for f in os.listdir("."):
        match = re.match("^([0-9]+-)?(.*\\.pdf)", f, re.IGNORECASE)
        if match:
            files.append((f, match.group(2)))

    # Shuffle and rename with sequential numbers
    random.shuffle(files)
    for i in range(len(files)):
        name = "{:02d}-{}".format(i + 1, files[i][1])
        os.rename(files[i][0], name)

    print(f"Shuffled and renamed {len(files)} PDF files")


def extract_names():
    """Extract and print names from numbered PDF files in order.

    Note: Only works if files have been renamed with the ##- prefix.
    """
    files = []
    for f in os.listdir("."):
        match = re.match("^(([0-9]+)-)?(([^_]+)_.*\\.pdf)", f, re.IGNORECASE)
        if match:
            files.append((int(match.group(2)), match.group(4)))

    files = sorted(files, key=lambda x: x[0])
    for i in range(len(files)):
        print(files[i][1])


def main():
    """Main entry point for random-order tool."""
    if len(sys.argv) > 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(__doc__)
            print("\nUsage:")
            print("  random-order          Shuffle PDFs in current directory")
            print("  random-order extract  Extract names from numbered PDFs")
            print("  random-order --help   Show this help message")
            return 0
        elif sys.argv[1] == "extract":
            extract_names()
            return 0

    # Default action: shuffle
    shuffle()
    return 0


if __name__ == "__main__":
    sys.exit(main())
