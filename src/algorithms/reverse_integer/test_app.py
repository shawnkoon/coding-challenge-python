import unittest
from .app import ReverseInteger


class ReverseIntegerTest(unittest.TestCase):
    def setUp(self):
        self.tester = ReverseInteger()

    def test_case_1(self):
        arg = 123
        res = 321
        self.assertEqual(self.tester.reverse(arg), res)

    def test_case_2(self):
        arg = -120
        res = -21
        self.assertEqual(self.tester.reverse(arg), res)

    def test_case_3(self):
        arg = 1534236469
        res = 0
        self.assertEqual(self.tester.reverse(arg), res)
