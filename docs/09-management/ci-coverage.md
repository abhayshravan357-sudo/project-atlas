# Phase 6.1 — CI and Coverage

## What was added

| File | Purpose |
|------|---------|
| `.github/workflows/ci.yml` | GitHub Actions CI pipeline (test + lint) |
| `pyproject.toml` | Added `[tool.coverage.*]` configuration |

## Why it was needed

Phase 6.1's first requirement is a repeatable automated quality baseline. Before this change, the project had tests but no CI pipeline and no coverage measurement, so changes could silently break functionality without detection.

## Technology / package involved

- **GitHub Actions** (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) — CI platform
- **Python 3.10 / 3.11 / 3.12** — tested matrix
- **pytest** — test execution
- **coverage 7.17.0** — coverage measurement and reporting
- **ruff** — linting

## Where it exists in the repository

- `.github/workflows/ci.yml` — CI pipeline definition
- `pyproject.toml` — coverage configuration under `[tool.coverage.*]`

## How it works

### CI pipeline (`ci.yml`)

Triggers on push to `main` and pull requests to `main`.

**test job** (Python 3.10/3.11/3.12 matrix):
1. Checks out the repository.
2. Sets up the Python version.
3. Installs pytest and coverage.
4. Runs `coverage run -m pytest` then `coverage report --fail-under=80` (fails the job if coverage drops below 80%).
5. Uploads the HTML coverage report as a workflow artifact.

**lint job** (Python 3.12):
1. Installs ruff.
2. Runs `ruff check src tests`.

### Coverage configuration (`pyproject.toml`)

- `source = ["src/atlas"]` — measures only the Atlas package, not tests.
- `branch = true` — measures branch coverage, not just line coverage.
- `fail_under = 80` — CI fails if coverage is below 80%.
- Excludes `pragma: no cover` lines and `if __name__ == "__main__":` blocks.
- HTML report written to `htmlcov/`.

## How to run and test it

### Locally

```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run -m pytest
coverage report --fail-under=80

# Generate HTML report
coverage html
# Open htmlcov/index.html in a browser
```

### In CI

Push to `main` or open a pull request; GitHub Actions runs the pipeline automatically.

## What the owner should learn

- Coverage below 80% fails CI, preventing under-tested code from merging.
- The matrix tests across Python 3.10–3.12 to catch version-specific issues.
- Linting (ruff) runs separately so style issues don't block test results.

## Limitations and alternatives

- **Limitation:** CI requires a GitHub repository with Actions enabled. If the project is not hosted on GitHub, the workflow file is still useful documentation but won't run automatically.
- **Alternative:** Use GitLab CI, CircleCI, or a local pre-commit hook instead.
- **Alternative to ruff:** Use flake8 or pylint; ruff was chosen for speed and Python 3.10+ compatibility.
