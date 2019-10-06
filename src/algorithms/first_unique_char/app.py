from typing import List


class FirstUniqueCharacter:
    """
    Source : https://leetcode.com/problems/first-unique-character-in-a-string/

    Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

    Examples:

        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
    Note: You may assume the string contain only lowercase letters.
    """

    def first_unique_char(self, s: List[str]) -> int:
        ht = {}

        for c in s:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1

        for i, c in enumerate(s):
            if ht[c] == 1:
                return i

        return -1
