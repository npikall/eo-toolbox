# Default command lists all available recipes
_default:
    @just --list

# Setup the virtual environment
venv:
    uv sync

# Setup the virtual environment for dev dependencies
venv-dev:
    uv sync --group dev

# Run the test suite
test:
    uv run pytest tests/ --color=yes --verbose

# Run the Linter (Ruff)
lint:
    uvx ruff check . --fix

# Run the Formatter (Ruff)
fmt:
    uvx ruff format . --check
    uvx ruff format .

# Run the Typechecker (ty)
types:
    uvx mypy .
# uvx ty check

# Run all Tools (Lint, Format, Typechecker)
style: lint fmt types

# Install pre-commit hooks
hooks:
    pre-commit install --hook-type commit-msg --hook-type pre-push
