import unittest
from .app import BinarySearchRotatedArray


class BinarySearchRotatedArrayTest(unittest.TestCase):
    def setUp(self):
        self.tester = BinarySearchRotatedArray()

    def test_case_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        exp = 4
        self.assertEqual(self.tester.search(nums, target), exp)

    def test_case_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        exp = -1
        self.assertEqual(self.tester.search(nums, target), exp)
