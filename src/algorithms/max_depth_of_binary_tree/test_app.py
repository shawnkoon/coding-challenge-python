import unittest
from .app import MaxDepthOfBinaryTree

from ...datastructures.TreeNode import TreeNode


class MaxDepthOfBinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.tester = MaxDepthOfBinaryTree()

    def test_case_1(self):
        payload = TreeNode.from_list([3, 9, 20, None, None, 15, 7])
        exp = 3
        self.assertEqual(self.tester.max_depth(payload), exp)

    def test_case_2(self):
        payload = TreeNode.from_list(
            [1, 4, 9, 4, None, 45, 7, None, None, None, None, 6, None, None, 5, 7])
        exp = 4
        self.assertEqual(self.tester.max_depth(payload), exp)
