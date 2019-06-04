from typing import List


class ListPermutations:
    """
    Source : https://leetcode.com/problems/permutations/

    Given a collection of distinct integers, return all possible permutations.

    Example:

    Input: [1,2,3]
    Output:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]
    """

    def function(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur, next_):
            if not next_:
                res.append(cur)
            else:
                for i, let in enumerate(next_):
                    backtrack([*cur, let], next_[:i] + next_[i + 1:])

        backtrack([], nums)

        return res
