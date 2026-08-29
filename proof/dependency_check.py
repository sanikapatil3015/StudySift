from pathlib import Path
import ast


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
REQUIREMENTS = PROJECT_ROOT / "requirements.txt"


STANDARD_LIBRARY_MODULES = {
    "argparse",
    "ast",
    "collections",
    "csv",
    "io",
    "json",
    "pathlib",
    "re",
    "tempfile",
    "unittest",
}


def get_imports(file_path):
    """Return imported top-level modules from a Python file."""

    tree = ast.parse(
        file_path.read_text(encoding="utf-8")
    )

    imports = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for item in node.names:
                imports.add(
                    item.name.split(".")[0]
                )

        elif isinstance(node, ast.ImportFrom):

            if node.module:
                imports.add(
                    node.module.split(".")[0]
                )

    return imports


def main():

    print("=" * 50)
    print("StudySift Dependency Proof")
    print("=" * 50)

    print()

    # Check requirements.txt
    requirements = REQUIREMENTS.read_text(
        encoding="utf-8"
    ).strip()

    if requirements:
        print("FAIL: requirements.txt is not empty.")
        print()
        print(requirements)
        return

    print("PASS: requirements.txt is empty.")

    print()

    # Check Python source imports
    all_imports = set()

    for file_path in SRC_DIR.glob("*.py"):

        imports = get_imports(file_path)

        all_imports.update(imports)

        print(
            f"{file_path.name}: "
            f"{', '.join(sorted(imports)) or 'no imports'}"
        )

    print()

    external = (
        all_imports
        - STANDARD_LIBRARY_MODULES
        - {"parser", "analyzer", "scorer", "generator", "main"}
    )

    if external:

        print(
            "FAIL: Possible external imports found:"
        )

        for module in sorted(external):
            print(f"  - {module}")

        return

    print(
        "PASS: No external third-party imports found."
    )

    print()

    print("Dependency proof successful.")


if __name__ == "__main__":
    main()