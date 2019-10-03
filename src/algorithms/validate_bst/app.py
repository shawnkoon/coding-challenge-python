from typing import List
from ...datastructures import TreeNode


class ValidateBST:
    """
    Source : https://leetcode.com/problems/validate-binary-search-tree/

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.


    Example 1:

      2

     / \\

    1   3

    Input: [2,1,3]
    Output: true
    Example 2:

       5

     /  \\

    1    4

        /  \\

        3   6

    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
    """

    def function1(self, root: TreeNode) -> bool:
        '''
        In-order style traversal.
        '''
        in_order_values = []
        stack = []

        # Populate In-order vals.
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                in_order_values.append(node.value)
                root = node.right

        # Checking
        min_val = float('-inf')

        for val in in_order_values:
            if val <= min_val:
                return False

            min_val = val

        return True

    def function2(self, root: TreeNode) -> bool:
        '''
        Pre-order style traversal.
        '''
        def pre_order_traversal(node: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
            # Base Case
            if not node:
                return True

            val = node.value

            # Pre-order
            if val <= min_val or val >= max_val:
                return False

            # Recursive Case
            if not pre_order_traversal(node.left, min_val, val):
                return False

            if not pre_order_traversal(node.right, val, max_val):
                return False

            return True

        return pre_order_traversal(root)
