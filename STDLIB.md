# StudySift Standard Library Map

StudySift is intentionally built without third-party Python packages.

All functionality is implemented using Python's standard library and
StudySift's own source modules.

## Standard Library Modules Used

| Standard Library Module | File | Purpose |
|---|---|---|
| `argparse` | `main.py` | Command-line interface |
| `pathlib` | `parser.py` | File and path handling |
| `re` | `analyzer.py` | Text processing and pattern matching |
| `collections` | `analyzer.py` | Keyword frequency counting |
| `json` | `generator.py` | JSON report generation |
| `csv` | `generator.py` | CSV report generation |
| `io` | `generator.py` | In-memory CSV output |
| `unittest` | `tests/` | Automated testing |

## Internal Modules

StudySift also imports its own modules:

- `parser`
- `analyzer`
- `scorer`
- `generator`

These are part of the StudySift source code and are not external
dependencies.

## Dependency Manifest

The project's `requirements.txt` file is intentionally empty.

No third-party Python package is required to run StudySift.

## Dependency Verification

The repository includes:

```text
proof/dependency_check.py