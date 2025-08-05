# EO-Toolbox

A loose collection of functions to work with Earth Observation Data.

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

Use the justfile aswell to run the linter, the formatter and the typechecker.
