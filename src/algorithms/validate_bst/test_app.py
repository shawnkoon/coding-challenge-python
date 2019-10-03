import unittest
from .app import ValidateBST
from typing import List

from ...datastructures import TreeNode


class ValidateBSTTest(unittest.TestCase):
    def setUp(self):
        self.tester = ValidateBST()

    def test_case_1(self):
        root = self.__create_tree([])
        self.assertTrue(self.tester.function1(root))
        self.assertTrue(self.tester.function2(root))

    def test_case_2(self):
        root = self.__create_tree([1, 1])
        self.assertFalse(self.tester.function1(root))
        self.assertFalse(self.tester.function2(root))

    def test_case_3(self):
        root = self.__create_tree([1, None, 1])
        self.assertFalse(self.tester.function1(root))
        self.assertFalse(self.tester.function2(root))

    def test_case_4(self):
        root = self.__create_tree([10, 5, 15, None, None, 6, 20])
        self.assertFalse(self.tester.function1(root))
        self.assertFalse(self.tester.function2(root))

    def test_case_5(self):
        root = self.__create_tree([2, 1, 3])
        self.assertTrue(self.tester.function1(root))
        self.assertTrue(self.tester.function2(root))

    def __create_tree(self, vals: List[int]) -> TreeNode:
        def helper(index: int = 0) -> TreeNode:
            if index >= len(vals) or not vals[index]:
                return None

            node = TreeNode(vals[index])

            # map left
            node.left = helper(index * 2 + 1)

            # map right
            node.right = helper(index * 2 + 2)

            return node

        if not vals:
            return None

        return helper()
