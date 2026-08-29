import unittest
import json

from src.generator import (
    create_json_report,
    create_csv_report
)


class TestGenerator(unittest.TestCase):

    def test_create_json_report(self):

        report = create_json_report(
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

        data = json.loads(report)

        self.assertEqual(
            data["file"],
            "sample.txt"
        )

        self.assertEqual(
            data["statistics"]["words"],
            100
        )

        self.assertEqual(
            data["score"],
            85
        )

        self.assertEqual(
            data["keywords"][0]["word"],
            "data"
        )

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


if __name__ == "__main__":
    unittest.main()