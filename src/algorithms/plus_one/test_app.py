import unittest
from .app import PlusOne


class PlusOneTest(unittest.TestCase):
    def setUp(self):
        self.tester = PlusOne()

    def test_case_1(self):
        digits = [9]
        exp = [1, 0]
        self.assertListEqual(self.tester.function(digits), exp)

    def test_case_2(self):
        digits = [1, 2, 3]
        exp = [1, 2, 4]
        self.assertListEqual(self.tester.function(digits), exp)

    def test_case_3(self):
        digits = [4, 3, 2, 1]
        exp = [4, 3, 2, 2]
        self.assertListEqual(self.tester.function(digits), exp)

    def test_case_4(self):
        digits = []
        exp = [1]
        self.assertListEqual(self.tester.function(digits), exp)
