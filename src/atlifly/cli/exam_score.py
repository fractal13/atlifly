#!/usr/bin/env python3
"""exam-score - Display exam percentage table by missed questions."""

from __future__ import annotations

import argparse
import sys


def _format_percent(value: float) -> str:
    return f"{value:.2f}%"


def _build_rows(total_questions: int) -> list[tuple[int, int, str]]:
    rows: list[tuple[int, int, str]] = []
    for missed in range(total_questions + 1):
        correct = total_questions - missed
        percent = (correct / total_questions) * 100
        rows.append((missed, correct, _format_percent(percent)))
    return rows


def _print_table(total_questions: int) -> None:
    headers = ("Missed", "Correct", "Percent")
    rows = _build_rows(total_questions)
    widths = [len(h) for h in headers]
    for missed, correct, percent in rows:
        widths[0] = max(widths[0], len(str(missed)))
        widths[1] = max(widths[1], len(str(correct)))
        widths[2] = max(widths[2], len(percent))

    def write_row(values: tuple[str, ...]) -> None:
        line = "  ".join(value.rjust(width) for value, width in zip(values, widths))
        print(line)

    write_row(headers)
    write_row(tuple("-" * width for width in widths))
    for missed, correct, percent in rows:
        write_row((str(missed), str(correct), percent))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Display exam percentage table by missed questions",
    )
    parser.add_argument(
        "total_questions",
        type=int,
        help="Total number of questions on the exam",
    )
    args = parser.parse_args()

    if args.total_questions <= 0:
        print("total_questions must be a positive integer", file=sys.stderr)
        return 1

    _print_table(args.total_questions)
    return 0


if __name__ == "__main__":
    sys.exit(main())
