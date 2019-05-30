import unittest
from .app import FindStringIndex


class FindStringIndexTest(unittest.TestCase):
    def setUp(self):
        self.tester = FindStringIndex()

    def test_case_1(self):
        haystack = 'hello'
        needle = 'll'
        exp = 2
        self.assertEqual(self.tester.function(haystack, needle), exp)

    def test_case_2(self):
        haystack = 'aaaaa'
        needle = 'bba'
        exp = -1
        self.assertEqual(self.tester.function(haystack, needle), exp)
