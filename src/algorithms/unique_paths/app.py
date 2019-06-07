class UniquePaths:
    """
    Source : https://leetcode.com/problems/unique-paths/

    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    How many possible unique paths are there?

    [R, , , , , , ]
    [ , , , , , , ]
    [ , , , , , ,F]

    R = Robot / F = Finish

    Above is a 7 x 3 grid. How many possible unique paths are there?

    Note: m and n will be at most 100.

    # Example 1:

    Input: m = 3, n = 2

    Output: 3

    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right

    # Example 2:

    Input: m = 7, n = 3

    Output: 28
    """

    def function(self, m: int, n: int) -> int:
        '''O(nm) Memoize Backtrack'''
        memo = {}

        def backtrack(i: int, j: int) -> int:
            res = 0
            # Base Case
            if i == m - 1 and j == n - 1:
                return 1

            if memo.get((i, j)):
                return memo[(i, j)]

            # Right
            if i + 1 < m:
                res += backtrack(i + 1, j)

            # Down
            if j + 1 < n:
                res += backtrack(i, j + 1)

            memo[(i, j)] = res
            return res

        return backtrack(0, 0)
