# StudySift Standard Library Map

StudySift intentionally avoids third-party dependencies.

The following standard-library modules provide functionality that
would commonly be implemented using external packages.

| Standard Library Module | Purpose in StudySift |
|---|---|
| argparse | Command-line interface |
| pathlib | File and path handling |
| json | JSON report generation |
| csv | CSV report generation |
| io | In-memory text streams for CSV generation |
| re | Text pattern matching |
| collections | Keyword frequency counting |
| unittest | Automated testing |

## Dependency Manifest

The project's `requirements.txt` file is intentionally empty.

No third-party Python package is required.

## Package Replacement Philosophy

Instead of installing external packages for basic document processing,
StudySift uses functionality already included with Python.

Examples:

- CLI framework → `argparse`
- JSON handling → `json`
- CSV generation → `csv`
- Text processing → `re`
- Frequency counting → `collections`
- Testing framework → `unittest`
- File handling → `pathlib`

This keeps the executable dependency surface limited to Python itself.