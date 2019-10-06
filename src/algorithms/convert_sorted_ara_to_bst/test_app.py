import unittest
from .app import ConvertSortedArrayToBST
from ...datastructures.TreeNode import TreeNode


class ConvertSortedArrayToBSTTest(unittest.TestCase):
    def setUp(self):
        self.tester = ConvertSortedArrayToBST()

    def test_case_1(self):
        payload = [-10, -3, 0, 5, 9]
        exp = [0, -3, 9, -10, None, 5]

        result = self.tester.get_tree(payload).to_list()

        self.assertListEqual(result, exp)

    def test_case_2(self):
        payload = [-13, -11, -10, -5, -3, 0, 1, 5, 30, 99]
        exp = [0, -10, 30, -11, -3, 5, 99, -13, None, -5, None, 1]

        result = self.tester.get_tree(payload).to_list()

        self.assertListEqual(result, exp)
