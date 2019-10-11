class LongestSubstringWithoutRepeat:
    """
    Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Given a string, find the length of the longest substring without repeating characters.

    Example 1:

        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
    Example 2:

        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
    Example 3:

        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
                Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def function(self, s: str) -> int:
        d = {}  # char : index
        cur_max = start_index = 0

        for cur_index, char in enumerate(s):
            # Check if exits && inside of the *NEW* substr
            if char in d and d[char] >= start_index:
                start_index = d[char] + 1
                d[char] = cur_index
                continue

            cur_max = max(cur_max, cur_index - start_index + 1)
            d[char] = cur_index

        return cur_max
