import unittest
from .app import SingleNumber


class SingleNumberTest(unittest.TestCase):
    def setUp(self):
        self.tester = SingleNumber()

    def test_case_1(self):
        payload = [2, 2, 1]
        exp = 1
        self.assertEqual(self.tester.singleNumber(payload), exp)

    def test_case_2(self):
        payload = [4, 1, 2, 1, 2]
        exp = 4
        self.assertEqual(self.tester.singleNumber(payload), exp)
