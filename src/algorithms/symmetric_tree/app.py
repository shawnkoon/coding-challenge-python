from typing import List

from ...datastructures.TreeNode import TreeNode


class SymmetricTree:
    """
    Source : https://leetcode.com/problems/symmetric-tree/

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

          1
         / \\
        2   2
       / \\ / \\
      3  4 4  3


    But the following [1,2,2,null,3,null,3] is not:

          1
         / \\
        2   2
         \\   \\
         3    3
    """

    def is_symmetric(self, root: TreeNode) -> bool:
        '''
        Use helper
        '''
        def helper(t1: TreeNode, t2: TreeNode) -> bool:
            if t1 is None and t2 is None:
                return True

            if t1 is None or t2 is None:
                return False

            return (t1.value == t2.value) and \
                helper(t1.right, t2.left) and \
                helper(t1.left, t2.right)

        return helper(root, root)
