import argparse

from parser import read_file

from analyzer import (
    count_words,
    count_characters,
    count_lines,
    count_sentences,
    count_paragraphs,
    get_keyword_frequency,
    average_word_length,
)

from scorer import calculate_score


def display_report(file_path, text):
    """
    Analyze the document and display
    the results in the terminal.
    """

    # --------------------------------
    # Calculate document statistics
    # --------------------------------

    words = count_words(text)

    characters = count_characters(text)

    lines = count_lines(text)

    sentences = count_sentences(text)

    paragraphs = count_paragraphs(text)

    average_length = average_word_length(text)

    # --------------------------------
    # Find keywords
    # --------------------------------

    keywords = get_keyword_frequency(text)

    # --------------------------------
    # Calculate document score
    # --------------------------------

    score = calculate_score(
        words,
        sentences,
        paragraphs,
        len(keywords)
    )

    # --------------------------------
    # Display report
    # --------------------------------

    print()

    print("=" * 50)

    print("              STUDYSIFT")

    print("       Zero-Dependency Analyzer")

    print("=" * 50)

    print()

    print(f"File: {file_path}")

    print()

    print("Document Statistics")

    print("-" * 30)

    print(f"Words:             {words}")

    print(f"Characters:        {characters}")

    print(f"Lines:             {lines}")

    print(f"Sentences:         {sentences}")

    print(f"Paragraphs:        {paragraphs}")

    print(
        f"Average word size: {average_length}"
    )

    print()

    print("Top Keywords")

    print("-" * 30)

    for word, frequency in keywords:

        print(
            f"{word:<20} {frequency}"
        )

    print()

    print("Document Score")

    print("-" * 30)

    print(f"Score: {score}/100")

    print()


def main():
    """
    Main function of StudySift.
    """

    # --------------------------------
    # Create command-line parser
    # --------------------------------

    parser = argparse.ArgumentParser(
        description=(
            "Analyze documents "
            "without external dependencies."
        )
    )

    # --------------------------------
    # Add file argument
    # --------------------------------

    parser.add_argument(
        "file",
        help="Path to the text file"
    )

    # --------------------------------
    # Read command-line arguments
    # --------------------------------

    args = parser.parse_args()

    # --------------------------------
    # Read and analyze the file
    # --------------------------------

    try:

        text = read_file(args.file)

        display_report(
            args.file,
            text
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )


# --------------------------------
# Start the program
# --------------------------------

if __name__ == "__main__":
    main()