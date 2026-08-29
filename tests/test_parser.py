import unittest
import tempfile
from pathlib import Path

from src.parser import (
    read_file,
    get_lines,
    get_paragraphs
)


class TestParser(unittest.TestCase):

    def test_read_file(self):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            encoding="utf-8"
        ) as file:

            file.write("Hello StudySift")
            file_path = file.name

        try:
            result = read_file(file_path)

            self.assertEqual(
                result,
                "Hello StudySift"
            )

        finally:
            Path(file_path).unlink()

    def test_get_lines(self):
        text = "Line one\nLine two\nLine three"

        result = get_lines(text)

        self.assertEqual(
            result,
            [
                "Line one",
                "Line two",
                "Line three"
            ]
        )

    def test_get_paragraphs(self):
        text = "First paragraph.\n\nSecond paragraph."

        result = get_paragraphs(text)

        self.assertEqual(
            result,
            [
                "First paragraph.",
                "Second paragraph."
            ]
        )


if __name__ == "__main__":
    unittest.main()