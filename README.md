# StudySift

StudySift is a zero-dependency document analysis CLI built entirely
with Python's standard library.

It analyzes text documents and provides:

- Word count
- Character count
- Line count
- Sentence count
- Paragraph count
- Average word length
- Keyword frequency
- Document score
- Text search
- JSON report generation
- CSV report generation

## Why Zero Dependency?

StudySift intentionally uses no third-party Python packages.

The project is built using only Python's standard library.

This makes the project:

- Easy to run
- Easy to audit
- Easy to reproduce
- Free from third-party package dependencies
- Less exposed to dependency and supply-chain risks

## Requirements

Python 3.x

No external packages are required.

## Installation

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_URL

Enter the project:

    cd StudySift

No pip install command is required.

## Usage

### Analyze a document

    python src/main.py examples/sample.txt

### Search the document

    python src/main.py examples/sample.txt --search data

### Generate JSON report

    python src/main.py examples/sample.txt --json result.json

### Generate CSV report

    python src/main.py examples/sample.txt --csv result.csv

### Show help

    python src/main.py --help

## Testing

Run all tests:

    python -m unittest discover -s tests -p "test_*.py"

## Project Structure

    StudySift/
    │
    ├── src/
    │   ├── parser.py
    │   ├── analyzer.py
    │   ├── scorer.py
    │   ├── generator.py
    │   └── main.py
    │
    ├── tests/
    │   ├── test_parser.py
    │   ├── test_analyzer.py
    │   ├── test_scorer.py
    │   └── test_generator.py
    │
    ├── examples/
    │   └── sample.txt
    │
    ├── requirements.txt
    ├── STDLIB.md
    └── README.md

## Zero Dependency Policy

`requirements.txt` is intentionally empty.

StudySift does not require third-party packages to build or run.

## License

This project is created for the Zero Dependency Hackathon 2026.