from typing import List


class ParenthesesGenerator:
    """
    Source : https://leetcode.com/problems/generate-parentheses/

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]
    """

    def function(self, n: int) -> List[str]:
        '''Approach with tree diagram & find pattern/restrictions.'''
        res = []

        def backtrack(s: str, left_count: int, right_count: int):
            if len(s) == n * 2:
                res.append(s)
                return
            if left_count < n:
                backtrack(s + '(', left_count + 1, right_count)
            if right_count < left_count:
                backtrack(s + ')', left_count, right_count + 1)

        backtrack('', 0, 0)
        return res
