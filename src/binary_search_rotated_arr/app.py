from typing import List


class BinarySearchRotatedArray:
    """
    Source : https://leetcode.com/problems/search-in-rotated-sorted-array/

    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array.
    Your algorithm's runtime complexity must be in the order of O(log n).

    Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    """

    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            md = lo + ((hi - lo) // 2)
            if nums[md] == target:  # base case
                return md

            if nums[lo] <= nums[md]:
                if nums[lo] <= target <= nums[md]:
                    hi = md - 1
                else:
                    lo = md + 1
            else:
                if nums[md] <= target <= nums[hi]:
                    lo = md + 1
                else:
                    hi = md - 1

        return -1
