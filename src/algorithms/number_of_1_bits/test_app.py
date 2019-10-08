import unittest
from .app import NumberOf1Bits


class NumberOf1BitsTest(unittest.TestCase):
    def setUp(self):
        self.tester = NumberOf1Bits()

    def test_case_1(self):
        payload = 11
        exp = 3

        self.assertEqual(self.tester.hammingWeight(payload), exp)

    def test_case_2(self):
        payload = 4294967293
        exp = 31

        self.assertEqual(self.tester.hammingWeight(payload), exp)
