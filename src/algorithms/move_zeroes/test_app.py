import unittest
from .app import MoveZeroes


class MoveZeroesTest(unittest.TestCase):
    def setUp(self):
        self.tester = MoveZeroes()

    def test_case_1(self):
        payload = [0, 1, 0, 3, 12]
        exp = [1, 3, 12, 0, 0]
        self.tester.function(payload)
        self.assertListEqual(payload, exp)
