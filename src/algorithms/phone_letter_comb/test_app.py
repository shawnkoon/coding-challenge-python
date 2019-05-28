import unittest
from .app import LetterCombinations


class LetterCombinationsTest(unittest.TestCase):
    def setUp(self):
        self.tester = LetterCombinations()

    def test_case_1(self):
        digits = "23"
        target = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertListEqual(self.tester.letterCombinations(digits), target)
        self.assertListEqual(
            self.tester.letterCombinations_iter(digits), target)
