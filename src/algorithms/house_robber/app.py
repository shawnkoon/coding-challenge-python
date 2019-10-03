from typing import List


class HouseRobber:
    """
    Source : https://leetcode.com/problems/house-robber/

    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

    Example 1:
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                Total amount you can rob = 1 + 3 = 4.

    ------

    Example 2:
    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    """

    def function(self, nums: List[int]) -> int:
        '''Dynamic Programming solution.'''
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        memo = {}

        def find_max(index=0):
            if index in memo:
                return memo[index]

            if index >= len(nums) - 2:
                return nums[index]

            next_targets = [nums[index] +
                            find_max(i) for i in range(index + 2, len(nums))]
            memo[index] = max(next_targets)

            return memo[index]

        return max(find_max(0), find_max(1))
