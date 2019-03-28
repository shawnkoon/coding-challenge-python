from typing import Dict, List, Optional


class TwoSum:
    """
    Source: https://leetcode.com/problems/two-sum/

    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.
    You may assume that each input would have *exactly* one solution,
    and you may not use the same element twice.

    Example:

    Given nums = `[2, 7, 11, 15]`, target = `9`,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return `[0, 1]`.
    """

    def two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        """Basic nested iteration solution"""
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return

    def two_sum_fast(self, nums: List[int], target: int) -> Optional[List[int]]:
        """Fast two sum solution using HashTable and one iteration"""
        hash_table: Dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = hash_table.get(target - num)
            if diff is None:
                hash_table[num] = i
            else:
                return [diff, i]
        return
