from typing import List


class GroupAnagrams:
    """
    Source : https://leetcode.com/problems/group-anagrams/

    Given an array of strings, group anagrams together.

    Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],

    Output:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]

    Note:

    - All inputs will be in lowercase.
    - The order of your output does not matter.

    """

    def function(self, strs: List[str]) -> List[List[str]]:
        '''[K: length of word] O(NK) '''
        ht = {}  # sorted_str : List[str]

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if ht.get(sorted_s):
                ht[sorted_s].append(s)
            else:
                ht[sorted_s] = [s]

        return [v for v in ht.values()]
