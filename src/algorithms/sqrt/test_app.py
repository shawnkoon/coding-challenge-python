import unittest
from .app import Sqrt


class SqrtTest(unittest.TestCase):
    def setUp(self):
        self.tester = Sqrt()

    def test_case_1(self):
        x = 4
        exp = 2
        self.assertEqual(self.tester.sqrt(x), exp)

    def test_case_2(self):
        x = 10
        exp = 3
        self.assertEqual(self.tester.sqrt(x), exp)

    def test_case_3(self):
        x = 2147395599
        exp = 46339
        self.assertEqual(self.tester.sqrt(x), exp)
