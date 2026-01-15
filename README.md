# atlifly

A collection of CLI tools to lift your burdens and help you fly.

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

## Available Tools

This package provides the following CLI commands:

- `random-order` - Shuffle and rename PDF files with numbered prefixes

## Usage

After installation, run any tool directly:

```bash
random-order          # Shuffle PDFs in current directory
random-order extract  # Extract names from numbered PDFs
random-order --help   # Show help
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
│       └── cli/
│           ├── __init__.py
│           └── random_order.py
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
