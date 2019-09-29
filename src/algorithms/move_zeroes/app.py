from typing import List


class MoveZeroes:
    """
    Source : https://leetcode.com/problems/move-zeroes/

    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
    """

    def function(self, nums: List[int]) -> None:
        available_spot = 0

        for i, n in enumerate(nums):
            if n:
                # Take the available spot
                nums[available_spot], nums[i] = nums[i], nums[available_spot]
                available_spot += 1
