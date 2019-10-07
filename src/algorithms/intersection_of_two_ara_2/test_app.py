import unittest
from .app import IntersectionOfTwoArrays2


class IntersectionOfTwoArrays2Test(unittest.TestCase):
    def setUp(self):
        self.tester = IntersectionOfTwoArrays2()

    def test_case_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        exp = [2, 2]

        self.assertListEqual(
            sorted(self.tester.function(nums1, nums2)), sorted(exp))

    def test_case_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        exp = [4, 9]

        self.assertListEqual(
            sorted(self.tester.function(nums1, nums2)), sorted(exp))

    def test_case_3(self):
        nums1 = [1, 2, 2, 1, 3, 2, 1]
        nums2 = [3, 2, 2]
        exp = [3, 2, 2]

        self.assertListEqual(
            sorted(self.tester.function(nums1, nums2)), sorted(exp))
