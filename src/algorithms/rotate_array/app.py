from typing import List


class RotateArray:
    """
    Source : https://leetcode.com/problems/rotate-array/

    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Example 1:

    Input: [1,2,3,4,5,6,7] and k = 3

    Output: [5,6,7,1,2,3,4]

    Explanation:

    rotate 1 steps to the right: [7,1,2,3,4,5,6]

    rotate 2 steps to the right: [6,7,1,2,3,4,5]

    rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:

    Input: [-1,-100,3,99] and k = 2

    Output: [3,99,-1,-100]

    Explanation:

    rotate 1 steps to the right: [99,-1,-100,3]

    rotate 2 steps to the right: [3,99,-1,-100]

    Note:

        - Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
        - Could you do it in-place with O(1) extra space?
    """

    def function(self, nums: List[int], k: int) -> None:
        # Edge Case
        if len(nums) < k:
            k = k - len(nums)

        # Reverse the array
        for i in range(len(nums) // 2):
            nums[i], nums[-1 - i] = nums[-1 - i], nums[i]

        # Reverse first kth
        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        # Reverse last kth
        for i in range((len(nums) - k) // 2):
            nums[k + i], nums[-1 - i] = nums[-1 - i], nums[k + i]
