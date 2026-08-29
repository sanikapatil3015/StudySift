import re
from collections import Counter


# Common words that are not very useful as keywords
STOP_WORDS = {
    "the",
    "is",
    "a",
    "an",
    "and",
    "are",
    "of",
    "to",
    "in",
    "for",
    "on",
    "with",
    "this",
    "that",
    "they",
    "we",
    "us",
    "it",
    "as",
    "be",
    "from",
    "using",
    "helps",
}


def get_words(text):
    """
    Extract words from the document.

    Converts everything to lowercase and
    removes punctuation.
    """

    return re.findall(
        r"\b[a-zA-Z]+\b",
        text.lower()
    )


def count_words(text):
    """
    Count the total number of words.
    """

    return len(get_words(text))


def count_characters(text):
    """
    Count the total number of characters.
    """

    return len(text)


def count_lines(text):
    """
    Count the number of lines.
    """

    return len(text.splitlines())


def count_sentences(text):
    """
    Count the number of sentences.
    """

    sentences = re.split(
        r"[.!?]+",
        text
    )

    return len([
        sentence
        for sentence in sentences
        if sentence.strip()
    ])


def count_paragraphs(text):
    """
    Count the number of paragraphs.
    """

    paragraphs = text.split("\n\n")

    return len([
        paragraph
        for paragraph in paragraphs
        if paragraph.strip()
    ])


def get_keyword_frequency(text, limit=10):
    """
    Find the most frequently used meaningful words.
    """

    words = get_words(text)

    # Remove common words and very short words
    meaningful_words = [
        word
        for word in words
        if word not in STOP_WORDS
        and len(word) > 2
    ]

    # Count how many times each word appears
    frequency = Counter(meaningful_words)

    # Return the most common words
    return frequency.most_common(limit)


def average_word_length(text):
    """
    Calculate the average length of a word.
    """

    words = get_words(text)

    if not words:
        return 0

    total_length = sum(
        len(word)
        for word in words
    )

    return round(
        total_length / len(words),
        2
    )