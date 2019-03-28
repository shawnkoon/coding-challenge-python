from typing import Dict


class Solution:
    """
    Source: https://leetcode.com/problems/valid-parentheses/
    Given a string containing just the characters '(', ')', '{', '}', '[', ']'
    determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.
    """

    def isValid(self, s: str) -> bool:
        parenth_dict: Dict[str, str] = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char not in parenth_dict.values():
                stack.append(char)
            else:
                if not stack:
                    return False

                open_p = stack.pop()

                if char != parenth_dict[open_p]:
                    return False

        if stack:
            return False

        return True
