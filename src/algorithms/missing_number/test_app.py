import unittest
from .app import MissingNumber


class MissingNumberTest(unittest.TestCase):
    def setUp(self):
        self.tester = MissingNumber()

    def test_case_1(self):
        payload = [3, 0, 1]
        exp = 2
        self.assertEqual(self.tester.find_missing_number(payload), exp)

    def test_case_2(self):
        payload = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        exp = 8
        self.assertEqual(self.tester.find_missing_number(payload), exp)
