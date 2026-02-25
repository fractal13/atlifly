#!/usr/bin/env python3
"""latex-build - Build LaTeX PDFs with rerun handling."""

from __future__ import annotations

import argparse
from importlib import resources
from pathlib import Path
import subprocess
import sys


def _normalize_target(target: str) -> tuple[Path, str]:
    path = Path(target)
    if path.suffix.lower() in {".pdf", ".tex"}:
        base = path.with_suffix("")
    else:
        base = path
    target_pdf = base.with_suffix(".pdf")
    return base, target_pdf.name


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build LaTeX PDFs with rerun handling",
    )
    parser.add_argument(
        "target",
        help="Target name: foo, foo.tex, or foo.pdf",
    )
    args = parser.parse_args()

    base, target_name = _normalize_target(args.target)
    cwd = base.parent if str(base.parent) not in {"", "."} else None
    tex_path = (cwd or Path(".")) / f"{base.name}.tex"
    if not tex_path.exists():
        location = f" in {cwd}" if cwd else ""
        print(f"Missing TeX file: {tex_path.name}{location}", file=sys.stderr)
        return 1

    script = resources.files("atlifly").joinpath("scripts", "latex_build.bash")
    with resources.as_file(script) as script_path:
        result = subprocess.run(
            ["bash", str(script_path), target_name],
            cwd=str(cwd) if cwd else None,
        )
        return result.returncode


if __name__ == "__main__":
    sys.exit(main())
