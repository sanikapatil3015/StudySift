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
    search_text
)

from scorer import calculate_score

from generator import (
    create_json_report,
    create_csv_report
)


def display_report(file_path, text):
    """
    Analyze the document and display
    the results in the terminal.
    """

    words = count_words(text)
    characters = count_characters(text)
    lines = count_lines(text)
    sentences = count_sentences(text)
    paragraphs = count_paragraphs(text)
    average_length = average_word_length(text)

    keywords = get_keyword_frequency(text)

    score = calculate_score(
        words,
        sentences,
        paragraphs,
        len(keywords)
    )

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
    print(f"Average word size: {average_length}")

    print()

    print("Top Keywords")
    print("-" * 30)

    for word, frequency in keywords:
        print(f"{word:<20} {frequency}")

    print()

    print("Document Score")
    print("-" * 30)
    print(f"Score: {score}/100")

    print()


def main():
    """
    Main function of StudySift.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Analyze documents "
            "without external dependencies."
        )
    )

    parser.add_argument(
        "file",
        help="Path to the text file"
    )

    parser.add_argument(
        "--search",
        help="Search for a word or phrase in the document"
    )

    parser.add_argument(
        "--json",
        help="Save the analysis report as a JSON file"
    )

    parser.add_argument(
        "--csv",
        help="Save the analysis report as a CSV file"
    )

    args = parser.parse_args()

    try:

        text = read_file(args.file)

        # --------------------------------
        # JSON export
        # --------------------------------

        if args.json:

            words = count_words(text)
            characters = count_characters(text)
            lines = count_lines(text)
            sentences = count_sentences(text)
            paragraphs = count_paragraphs(text)
            average_length = average_word_length(text)
            keywords = get_keyword_frequency(text)

            score = calculate_score(
                words,
                sentences,
                paragraphs,
                len(keywords)
            )

            report = create_json_report(
                args.file,
                words,
                characters,
                lines,
                sentences,
                paragraphs,
                average_length,
                keywords,
                score
            )

            with open(
                args.json,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(report)

            print(
                f"JSON report saved to: {args.json}"
            )

            return

        # --------------------------------
        # CSV export
        # --------------------------------

        if args.csv:

            words = count_words(text)
            characters = count_characters(text)
            lines = count_lines(text)
            sentences = count_sentences(text)
            paragraphs = count_paragraphs(text)
            average_length = average_word_length(text)
            keywords = get_keyword_frequency(text)

            score = calculate_score(
                words,
                sentences,
                paragraphs,
                len(keywords)
            )

            report = create_csv_report(
                args.file,
                words,
                characters,
                lines,
                sentences,
                paragraphs,
                average_length,
                keywords,
                score
            )

            with open(
                args.csv,
                "w",
                encoding="utf-8",
                newline=""
            ) as file:

                file.write(report)

            print(
                f"CSV report saved to: {args.csv}"
            )

            return

        # --------------------------------
        # Search
        # --------------------------------

        if args.search:

            results = search_text(
                text,
                args.search
            )

            print()

            print("=" * 50)
            print("              STUDYSIFT")
            print("              Search Results")
            print("=" * 50)

            print()

            print(
                f"Search term: {args.search}"
            )

            print(
                f"Found {len(results)} occurrence(s)"
            )

            print()

            if results:

                for result in results:

                    print(
                        f"Line {result['line_number']}:"
                    )

                    print(
                        result["line"]
                    )

                    print()

            else:

                print("No matches found.")

            return

        # --------------------------------
        # Normal analysis
        # --------------------------------

        display_report(
            args.file,
            text
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )


if __name__ == "__main__":
    main()