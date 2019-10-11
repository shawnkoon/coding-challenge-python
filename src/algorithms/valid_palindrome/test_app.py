import unittest
from .app import ValidatePalindrome


class ValidatePalindromeTest(unittest.TestCase):
    def setUp(self):
        self.tester = ValidatePalindrome()

    def test_case_1(self):
        s = "A man, a plan, a canal: Panama"

        self.assertTrue(self.tester.function(s))

    def test_case_2(self):
        s = "race a car"

        self.assertFalse(self.tester.function(s))

    def test_case_3(self):
        s = "0P"

        self.assertFalse(self.tester.function(s))
