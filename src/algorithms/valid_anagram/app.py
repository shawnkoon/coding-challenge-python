from typing import List


class ValidAnagram:
    """
    Source : https://leetcode.com/problems/valid-anagram/

    Given two strings s and t , write a function to determine if t is an anagram of s.

    Example 1:

        Input: s = "anagram", t = "nagaram"
        Output: true
    Example 2:

        Input: s = "rat", t = "car"
        Output: false
    Note:
    You may assume the string contains only lowercase alphabets.

    Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
    """

    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ht = {}

        for l in s:
            try:
                s_ht[l] += 1
            except Exception:
                s_ht[l] = 1

        for l in t:
            try:
                s_ht[l] -= 1
                if s_ht[l] < 0:
                    return False
            except Exception:
                return False

        return True
