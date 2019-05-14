from typing import List


class ThreeSum:
    """
    Source : https://leetcode.com/problems/3sum/

    Given an array `nums` of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    Note:

    The solution set must not contain duplicate triplets.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        len_ = len(nums)
        for i in range(len_):
            if i > len_ - 2:
                break
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len_ - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]

                if tot < 0:
                    l += 1
                elif tot > 0:
                    r -= 1
                else:
                    # moves l, r to a new values since a = -b - c is unique to three numbers.
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res
