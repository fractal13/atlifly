# atlifly

A collection of CLI tools to lift your burdens and help you fly.

## Available Tools

- **`random-order`** - Shuffle and rename PDF files with numbered prefixes
- **`latex-build`** - Build LaTeX PDFs with automatic reruns and cleanup
- **`exam-score`** - Display exam percentage table by missed questions

## Usage

### random-order

Shuffle and rename PDF files with numbered prefixes.

```bash
# Shuffle PDFs in current directory
random-order

# Shuffle PDFs in a specific directory
random-order ~/Documents/pdfs

# Extract names from numbered PDFs in current directory
random-order extract

# Extract names from numbered PDFs in a specific directory
random-order extract ~/Documents/pdfs

# Show help
random-order --help
```

### latex-build

Build a LaTeX PDF, rerunning as directed by the log file. Requires `pdflatex` on PATH.

```bash
# Build a PDF by base name
latex-build slides

# Build using an explicit .tex or .pdf name
latex-build slides.tex
latex-build slides.pdf

# Build a PDF in a specific directory
latex-build ~/Documents/tex/slides.pdf
```

### exam-score

Display a table of percentages based on missed questions.

```bash
# Display a table for a 40-question exam
exam-score 40
```


## Installation

Install with pipx (recommended):

```bash
pipx install .
```

Or install with pip:

```bash
pip install .
```

For development (editable install):

```bash
pipx install -e .
```

## Adding New Tools

To add a new tool:

1. Create a new Python file in `src/atlifly/cli/` (e.g., `mytool.py`)
2. Add a `main()` function that will serve as the entry point
3. Add a new entry in `pyproject.toml` under `[project.scripts]`:
   ```toml
   mytool = "atlifly.cli.mytool:main"
   ```
4. Reinstall the package: `pipx reinstall atlifly` or `pipx install -e .` for development

## Project Structure

```
atlifly/
├── src/
│   └── atlifly/
│       ├── __init__.py
│       ├── cli/
│       │   ├── __init__.py
│       │   ├── latex_build.py
│       │   ├── exam_score.py
│       │   └── random_order.py
│       └── scripts/
│           └── latex_build.bash
├── pyproject.toml
└── README.md
```

## Development

Clone the repository and install in development mode:

```bash
git clone <repository-url>
cd atlifly
pipx install -e .
```

## License

See LICENSE file for details.
