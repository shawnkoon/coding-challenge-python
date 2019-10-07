from typing import List
from ...datastructures.TreeNode import TreeNode


class ConvertSortedArrayToBST:
    """
    Source : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

    Example:

        Given the sorted array: [-10,-3,0,5,9],

        One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

             0
            / \\
         -3   9
         /   /
       -10  5
    """

    def get_tree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid_i = len(nums) // 2

        new_node = TreeNode(nums[mid_i])

        new_node.left = self.get_tree(nums[:mid_i])
        new_node.right = self.get_tree(nums[mid_i + 1:])

        return new_node
