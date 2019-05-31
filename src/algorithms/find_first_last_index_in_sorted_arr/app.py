from typing import List


class FindFirstLastIndexInSortedArray:
    """
    Source : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
    """

    def function(self, nums: List[int], target: int) -> List[int]:
        '''O(log n) using binary search twice.'''
        l = 0
        r = len(nums) - 1
        res = []

        if not nums:
            return [-1, -1]

        while l < r:
            md = l + ((r - l) // 2)

            if nums[md] < target:
                l = md + 1
            elif nums[md] > target:
                r = md - 1
            else:
                # if left is also target, reduce
                if nums[md - 1] == target:
                    r = md - 1
                else:
                    res.append(md)
                    break

        if nums[l] == target and not res:
            res.append(l)

        if not res:
            return [-1, -1]

        l = 0
        r = len(nums) - 1

        while l < r:
            md = l + ((r - l) // 2)

            if nums[md] < target:
                l = md + 1
            elif nums[md] > target:
                r = md - 1
            else:
                # if right is also target, reduce
                if nums[md + 1] == target:
                    l = md + 1
                else:
                    res.append(md)
                    break

        if nums[r] == target and len(res) == 1:
            res.append(r)

        return res
