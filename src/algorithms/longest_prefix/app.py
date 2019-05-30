from typing import cast, List


class Solution:
    """
    Source : https://leetcode.com/problems/longest-common-prefix/
    Write a function to find the longest common prefix string
    amongst an array of strings.
    If there is no common prefix, return an empty string `""`.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res: str = ""

        if not strs:
            return res

        for i in range(len(min(strs))):
            char = None
            for word in strs:
                if char is None:
                    char = word[i]
                if word[i] != char:
                    return res
            res += cast(str, char)

        return res
