import unittest
from .app import SymmetricTree
from ...datastructures.TreeNode import TreeNode


class SymmetricTreeTest(unittest.TestCase):
    def setUp(self):
        self.tester = SymmetricTree()

    def test_case_1(self):
        payload = TreeNode.from_list([1, 2, 2, 3, 4, 4, 3])

        self.assertTrue(self.tester.is_symmetric(payload))

    def test_case_2(self):
        payload = TreeNode.from_list([1, 2, 2, None, 3, None, 3])

        self.assertFalse(self.tester.is_symmetric(payload))
