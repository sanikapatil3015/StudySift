import unittest

from src.analyzer import (
    count_words,
    count_characters,
    count_lines,
    count_sentences,
    count_paragraphs,
    get_keyword_frequency,
    average_word_length,
    search_text
)


class TestAnalyzer(unittest.TestCase):

    def test_count_words(self):
        text = "Hello StudySift World"

        result = count_words(text)

        self.assertEqual(result, 3)

    def test_count_characters(self):
        text = "Hello"

        result = count_characters(text)

        self.assertEqual(result, 5)

    def test_count_lines(self):
        text = "Line one\nLine two\nLine three"

        result = count_lines(text)

        self.assertEqual(result, 3)

    def test_count_sentences(self):
        text = "Hello world. How are you?"

        result = count_sentences(text)

        self.assertEqual(result, 2)

    def test_count_paragraphs(self):
        text = "First paragraph.\n\nSecond paragraph."

        result = count_paragraphs(text)

        self.assertEqual(result, 2)

    def test_get_keyword_frequency(self):
        text = "Python Python Java Python"

        result = get_keyword_frequency(text)

        self.assertEqual(result[0], ("python", 3))

    def test_average_word_length(self):
        text = "Hello world"

        result = average_word_length(text)

        self.assertEqual(result, 5.0)

    def test_search_text(self):
        text = "Python is easy.\nPython is powerful."

        result = search_text(text, "Python")

        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()