import unittest
from .app import TrapRainWater


class TrapRainWaterTest(unittest.TestCase):
    def setUp(self):
        self.tester = TrapRainWater()

    def test_case_1(self):
        input_ = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        exp = 6
        self.assertEqual(self.tester.function(input_), exp)

    def test_case_2(self):
        input_ = [6, 2, 5, 2, 1]
        exp = 3
        self.assertEqual(self.tester.function(input_), exp)
