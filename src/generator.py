import json
import csv
import io

def create_json_report(
    file_path,
    words,
    characters,
    lines,
    sentences,
    paragraphs,
    average_length,
    keywords,
    score
):
    """
    Create a JSON report containing
    document analysis results.
    """

    report = {
        "file": file_path,

        "statistics": {
            "words": words,
            "characters": characters,
            "lines": lines,
            "sentences": sentences,
            "paragraphs": paragraphs,
            "average_word_length": average_length
        },

        "keywords": [
            {
                "word": word,
                "frequency": frequency
            }
            for word, frequency in keywords
        ],

        "score": score
    }

    return json.dumps(
        report,
        indent=4
    )
def create_csv_report(
    file_path,
    words,
    characters,
    lines,
    sentences,
    paragraphs,
    average_length,
    keywords,
    score
):
    """
    Create a CSV report containing
    document analysis results.
    """

    output = io.StringIO()

    writer = csv.writer(output)

    # Document information
    writer.writerow(["StudySift Report"])
    writer.writerow([])

    writer.writerow(["File", file_path])
    writer.writerow([])

    # Statistics
    writer.writerow(["Statistic", "Value"])

    writer.writerow(["Words", words])
    writer.writerow(["Characters", characters])
    writer.writerow(["Lines", lines])
    writer.writerow(["Sentences", sentences])
    writer.writerow(["Paragraphs", paragraphs])
    writer.writerow(["Average Word Length", average_length])
    writer.writerow(["Score", score])

    writer.writerow([])

    # Keywords
    writer.writerow(["Keyword", "Frequency"])

    for word, frequency in keywords:

        writer.writerow([
            word,
            frequency
        ])

    return output.getvalue()
    def test_create_csv_report(self):

        report = create_csv_report(
            "sample.txt",
            100,
            500,
            10,
            5,
            2,
            5.0,
            [
                ("data", 5),
                ("algorithm", 3)
            ],
            85
        )

        self.assertIn(
            "sample.txt",
            report
        )

        self.assertIn(
            "Words,100",
            report
        )

        self.assertIn(
            "Score,85",
            report
        )

        self.assertIn(
            "data,5",
            report
        )