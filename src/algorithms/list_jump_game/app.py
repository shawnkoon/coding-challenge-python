from typing import List


class ListJumpGame:
    """
    Source : https://leetcode.com/problems/jump-game/

    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.

    Example 1:

    Input: [2,3,1,1,4]

    Output: true

    - Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:

    Input: [3,2,1,0,4]

    Output: false

    - Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
    """

    def function(self, nums: List[int]) -> bool:
        '''O(n) Memoized backtrack'''
        memo = {}

        if not nums:
            return False

        def backtrack(cur_i: int) -> bool:
            memo[cur_i] = 1

            # base case
            if cur_i == len(nums) - 1:
                return True

            t = []

            for i in reversed(range(1, nums[cur_i] + 1)):
                if memo.get(i + cur_i):
                    break

                if i + cur_i < len(nums):
                    t.append(backtrack(cur_i + i))

            return any(t)

        return backtrack(0)

    def function2(self, nums: List[int]) -> bool:
        '''O(n) Greedy algorithm'''
        last_i = len(nums) - 1
        for i in reversed(range(0, len(nums))):
            if nums[i] + i >= last_i:
                last_i = i

        return last_i == 0
