import unittest
from .app import RotateMatrix


class RotateMatrixTest(unittest.TestCase):
    def setUp(self):
        self.tester = RotateMatrix()

    def test_case_1(self):
        test_cases = [
            (self.tester.function, 'function'),
            (self.tester.function2, 'function2'),
        ]
        exp = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        for fn, desc in test_cases:
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            fn(matrix)
            self.assertListEqual(matrix, exp, desc)

    def test_case_2(self):
        test_cases = [
            (self.tester.function, 'function'),
            (self.tester.function2, 'function2'),
        ]
        exp = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]

        for fn, desc in test_cases:
            matrix = [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16]
            ]
            fn(matrix)
            self.assertListEqual(matrix, exp, desc)
