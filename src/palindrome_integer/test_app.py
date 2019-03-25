import unittest
from .app import Solution


class PalindromeIntegerTest(unittest.TestCase):
    def setUp(self):
        self.tester = Solution()

    def test_case_1(self):
        arg = 121
        res = True
        self.assertEqual(self.tester.isPalindrome(arg), res)
        self.assertEqual(self.tester.isPalindrome_int(arg), res)

    def test_case_2(self):
        arg = -121
        res = False
        self.assertEqual(self.tester.isPalindrome(arg), res)
        self.assertEqual(self.tester.isPalindrome_int(arg), res)

    def test_case_3(self):
        arg = 10
        res = False
        self.assertEqual(self.tester.isPalindrome(arg), res)
        self.assertEqual(self.tester.isPalindrome_int(arg), res)
