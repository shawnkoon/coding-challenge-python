import unittest
from .app import MergeSortedArray


class MergeSortedArrayTest(unittest.TestCase):
    def setUp(self):
        self.tester = MergeSortedArray()

    def test_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        exp = [1, 2, 2, 3, 5, 6]
        self.tester.function(nums1, m, nums2, n)

        self.assertListEqual(nums1, exp)
