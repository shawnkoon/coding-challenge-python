from typing import List


class Solution:
    """
    Source: https://leetcode.com/problems/maximum-subarray/

    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4]

    Output: 6

    Explanation: [4,-1,2,1] has the largest sum = 6.
    """

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)
