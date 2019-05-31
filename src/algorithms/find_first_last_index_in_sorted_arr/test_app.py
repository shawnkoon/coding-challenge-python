import unittest
from .app import FindFirstLastIndexInSortedArray


class FindFirstLastIndexInSortedArrayTest(unittest.TestCase):
    def setUp(self):
        self.tester = FindFirstLastIndexInSortedArray()

    def test_case_1(self):
        ara = [5, 7, 7, 8, 8, 10]
        target = 8
        exp = [3, 4]
        self.assertListEqual(self.tester.function(ara, target), exp)

    def test_case_2(self):
        ara = [5, 7, 7, 8, 8, 10]
        target = 6
        exp = [-1, -1]
        self.assertListEqual(self.tester.function(ara, target), exp)

    def test_case_3(self):
        ara = []
        target = 0
        exp = [-1, -1]
        self.assertListEqual(self.tester.function(ara, target), exp)
