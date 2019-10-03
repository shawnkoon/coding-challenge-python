class ClimbingStairs:
    """
    Source : https://leetcode.com/problems/climbing-stairs/

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.

    Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """

    def function(self, n: int) -> int:
        '''
        Memoize recursive solution.

        Thinking of steps as an array.
        '''
        memo = {}

        def find_total(cur: int = 0) -> int:
            # Memo
            if cur in memo:
                return memo[cur]

            # Base Case
            if n - cur <= 2:
                return n - cur

            memo[cur] = find_total(cur + 1) + find_total(cur + 2)

            return memo[cur]

        return find_total()
