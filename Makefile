.PHONY: install install-dev uninstall reinstall help

help:
	@echo "Available targets:"
	@echo "  make install      - Install package with pipx"
	@echo "  make install-dev  - Install package in development mode with pipx"
	@echo "  make reinstall    - Reinstall package with pipx"
	@echo "  make uninstall    - Uninstall package with pipx"

install:
	pipx install .

install-dev:
	pipx install -e .

reinstall:
	pipx reinstall atlifly

uninstall:
	pipx uninstall atlifly
