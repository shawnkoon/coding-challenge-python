import unittest
from .app import TwoSum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.tester = TwoSum()

    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        res = [0, 1]
        self.assertEqual(self.tester.two_sum(nums, target), res)
        self.assertEqual(self.tester.two_sum_fast(nums, target), res)

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        res = [1, 2]
        self.assertEqual(self.tester.two_sum(nums, target), res)
        self.assertEqual(self.tester.two_sum_fast(nums, target), res)
