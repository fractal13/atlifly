#!/usr/bin/env python3
"""Random Order - Shuffle and rename PDF files with numbered prefixes.

This tool helps randomize the order of PDF files in a directory by:
1. Cleaning up filenames (removing spaces, special characters)
2. Shuffling the files randomly
3. Renaming them with sequential number prefixes (01-, 02-, etc.)
"""

import argparse
import os
import re
import random
import sys


def shuffle(directory="."):
    """Shuffle PDF files in the specified directory with numbered prefixes.

    Args:
        directory: Directory to process (default: current directory)
    """
    # First pass: clean up filenames
    for f in os.listdir(directory):
        match = re.match("^([0-9]+-)?(.*\\.pdf)", f, re.IGNORECASE)
        if match:
            old_path = os.path.join(directory, f)
            new_name = f.replace(" ", "-")
            new_name = new_name.replace("'", "_")
            new_name = new_name.replace("(", "_")
            new_name = new_name.replace(")", "_")
            if new_name != f:
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)

    # Second pass: collect PDF files
    files = []
    for f in os.listdir(directory):
        match = re.match("^([0-9]+-)?(.*\\.pdf)", f, re.IGNORECASE)
        if match:
            files.append((f, match.group(2)))

    # Shuffle and rename with sequential numbers
    random.shuffle(files)
    for i in range(len(files)):
        name = "{:02d}-{}".format(i + 1, files[i][1])
        old_path = os.path.join(directory, files[i][0])
        new_path = os.path.join(directory, name)
        os.rename(old_path, new_path)

    print(f"Shuffled and renamed {len(files)} PDF files in {directory}")


def extract_names(directory="."):
    """Extract and print names from numbered PDF files in order.

    Args:
        directory: Directory to process (default: current directory)

    Note: Only works if files have been renamed with the ##- prefix.
    """
    files = []
    for f in os.listdir(directory):
        match = re.match("^(([0-9]+)-)?(([^_]+)_.*\\.pdf)", f, re.IGNORECASE)
        if match:
            files.append((int(match.group(2)), match.group(4)))

    files = sorted(files, key=lambda x: x[0])
    for i in range(len(files)):
        print(files[i][1])


def main():
    """Main entry point for random-order tool."""
    parser = argparse.ArgumentParser(
        description="Shuffle and rename PDF files with numbered prefixes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  random-order                    Shuffle PDFs in current directory
  random-order ~/Documents/pdfs   Shuffle PDFs in specified directory
  random-order extract            Extract names from numbered PDFs
  random-order extract ~/pdfs     Extract names from specified directory
        """,
    )

    parser.add_argument(
        "action",
        nargs="?",
        default="shuffle",
        choices=["shuffle", "extract"],
        help="Action to perform: shuffle PDFs (default) or extract names",
    )

    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to process (default: current directory)",
    )

    args = parser.parse_args()

    if args.action == "extract":
        extract_names(args.directory)
    else:
        shuffle(args.directory)

    return 0


if __name__ == "__main__":
    sys.exit(main())
