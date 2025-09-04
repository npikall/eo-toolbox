# EO-Toolbox

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
![GitHub repo size](https://img.shields.io/github/repo-size/npikall/eo-toolbox)
![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnpikall%2Feo-toolbox%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.version&label=version)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/npikall/eo-toolbox/ci.yml)

A loose collection of functions to work with Earth Observation Data.

## Useage

Use the following command to install the toolbox.

```bash
uv pip install git+https://github.com/npikall/eo-toolbox
```

## Development

Make sure to have the `Just` Taskrunner installed, aswell as `uv`

After you have cloned the repo you might want to run the following commands:

```bash
# Install the dependencies
just venv-dev

# Install pre-commit hooks
just hooks
```

To run the Test suite execute:

```bash
just test
```

Use the `justfile` aswell to run the linter, the formatter and the typechecker.
