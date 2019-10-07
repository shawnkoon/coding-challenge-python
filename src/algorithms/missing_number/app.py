from typing import List


class MissingNumber:
    """
    Source : https://leetcode.com/problems/missing-number/

    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    Example 1:

        Input: [3,0,1]
        Output: 2
    Example 2:

        Input: [9,6,4,2,3,5,7,0,1]
        Output: 8
    Note:
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
    """

    def find_missing_number(self, nums: List[int]) -> int:
        '''
        Using the sumation forumula = N(N + 1)/2
        '''
        exp_sum = len(nums) * (len(nums) + 1) // 2
        act_sum = sum(nums)

        return exp_sum - act_sum
