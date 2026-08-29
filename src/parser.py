from pathlib import Path


def read_file(file_path):
    """
    Read the contents of a text file.

    Args:
        file_path: Path of the file to read.

    Returns:
        The complete text of the file.
    """

    path = Path(file_path)

    # Check if the file exists
    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    # Check if the path is actually a file
    if not path.is_file():
        raise ValueError(
            f"Not a file: {file_path}"
        )

    # Read and return the file contents
    return path.read_text(encoding="utf-8")


def get_lines(text):
    """
    Return all lines from the document.
    """

    return text.splitlines()


def get_paragraphs(text):
    """
    Split the document into paragraphs.
    """

    paragraphs = text.split("\n\n")

    return [
        paragraph.strip()
        for paragraph in paragraphs
        if paragraph.strip()
    ]