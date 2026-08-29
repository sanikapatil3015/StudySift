import unittest

from src.scorer import calculate_score


class TestScorer(unittest.TestCase):

    def test_calculate_score(self):

        result = calculate_score(
            100,
            10,
            5,
            10
        )

        self.assertIsInstance(
            result,
            (int, float)
        )

        self.assertGreaterEqual(
            result,
            0
        )

        self.assertLessEqual(
            result,
            100
        )

    def test_score_is_number(self):

        result = calculate_score(
            50,
            5,
            2,
            5
        )

        self.assertIsInstance(
            result,
            (int, float)
        )


if __name__ == "__main__":
    unittest.main()