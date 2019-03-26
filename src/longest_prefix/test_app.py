import unittest
from .app import Solution


class LongestPrefixTest(unittest.TestCase):
    def setUp(self):
        self.tester = Solution()

    def test_case_1(self):
        input_str = ["flower", "flow", "flight"]
        output = "fl"
        self.assertEqual(self.tester.longestCommonPrefix(input_str), output)

    def test_case_2(self):
        input_str = ["dog", "racecar", "car"]
        output = ""
        self.assertEqual(self.tester.longestCommonPrefix(input_str), output)
