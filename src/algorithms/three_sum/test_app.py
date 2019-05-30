import unittest
from .app import ThreeSum


class ThreeSumTest(unittest.TestCase):
    def setUp(self):
        self.tester = ThreeSum()

    def test_case_1(self):
        input_ = [-1, 0, 1, 2, -1, -4]
        target = [[-1, -1, 2], [-1, 0, 1]]
        self.assertListEqual(self.tester.threeSum(input_), target)

    def test_case_2(self):
        '''With large input'''
        input_ = [1, -2, -5, -13, -10, -11, 0, -12, -11, 13, -4, 9, 8, 10, -7, 3, -9, -12, -7,
                  8, -2, -12, 1, -10, -15, -8, 5, 14, -7, -8, -8, 9, -3, -6, 3, -5, -1, -11, -10, 3, -13]
        target = [[-15, 1, 14], [-15, 5, 10], [-13, -1, 14], [-13, 0, 13], [-13, 3, 10], [-13, 5, 8], [-12, -2, 14], [-12, -1, 13], [-12, 3, 9], [-11, -3, 14], [-11, -2, 13], [-11, 1, 10], [-11, 3, 8], [-10, -4, 14], [-10, -3, 13], [-10, 0, 10], [-10, 1, 9], [-9, -5, 14], [-9, -4, 13], [-9, -1, 10], [-9, 0, 9], [-9, 1, 8], [-8, -6, 14],
                  [-8, -5, 13], [-8, -2, 10], [-8, -1, 9], [-8, 0, 8], [-8, 3, 5], [-7, -7, 14], [-7, -6, 13], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, 1, 5], [-6, 3, 3], [-5, -5, 10], [-5, -4, 9], [-5, -3, 8], [-5, 0, 5], [-4, -1, 5], [-4, 1, 3], [-3, -2, 5], [-3, 0, 3], [-2, -1, 3], [-2, 1, 1], [-1, 0, 1]]
        self.assertListEqual(self.tester.threeSum(input_), target)