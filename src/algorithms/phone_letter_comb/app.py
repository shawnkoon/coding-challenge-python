from typing import List


class LetterCombinations:
    """
    Source : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent.

    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        output = []

        if digits == '':
            return []

        def backtrack(cur_str, next_str):
            if next_str == '':
                output.append(cur_str)
            else:
                for let in phone[next_str[0]]:
                    backtrack(cur_str + let, next_str[1:])

        backtrack("", digits)

        return output

    def letterCombinations_iter(self, digits: str) -> List[str]:
        if digits == '':
            return []

        res = ['']
        num_pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for digit in digits:
            temp = []
            for r in res:
                for l in num_pad[digit]:
                    temp.append(r + l)
            res = temp

        return res
