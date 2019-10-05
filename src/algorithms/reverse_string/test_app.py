import unittest
from .app import ReverseString


class ReverseStringTest(unittest.TestCase):
    def setUp(self):
        self.tester = ReverseString()

    def test_case_1(self):
        payload = ['h', 'e', 'l', 'l', 'o']
        exp = ['o', 'l', 'l', 'e', 'h']

        self.tester.reverseString(payload)

        self.assertListEqual(payload, exp)

    def test_case_2(self):
        payload = ['H', 'a', 'n', 'n', 'a', 'h']
        exp = ['h', 'a', 'n', 'n', 'a', 'H']

        self.tester.reverseString(payload)

        self.assertListEqual(payload, exp)
