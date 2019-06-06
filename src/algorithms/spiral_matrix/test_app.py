import unittest
from .app import SpiralMatrix


class SpiralMatrixTest(unittest.TestCase):
    def setUp(self):
        self.tester = SpiralMatrix()

    def test_case_1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        exp = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertListEqual(self.tester.function(matrix), exp)

    def test_case_2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        exp = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertListEqual(self.tester.function(matrix), exp)
