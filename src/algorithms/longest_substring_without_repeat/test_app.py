import unittest
from .app import LongestSubstringWithoutRepeat


class LongestSubstringWithoutRepeatTest(unittest.TestCase):
    def setUp(self):
        self.tester = LongestSubstringWithoutRepeat()

    def test_case_1(self):
        s = "abcabcbb"
        exp = 3

        self.assertEqual(self.tester.function(s), exp)

    def test_case_2(self):
        s = "bbbbb"
        exp = 1

        self.assertEqual(self.tester.function(s), exp)

    def test_case_3(self):
        s = "pwwkew"
        exp = 3

        self.assertEqual(self.tester.function(s), exp)

    def test_case_4(self):
        s = "zababczd"
        exp = 5

        self.assertEqual(self.tester.function(s), exp)
