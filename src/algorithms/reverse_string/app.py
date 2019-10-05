from typing import List


class ReverseString:
    """
    Source : https://leetcode.com/problems/reverse-string/

    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.



    Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    Example 2:

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
    """

    def reverseString(self, string: List[str]) -> None:
        '''Iterate till half way.'''
        for i in range(len(string) // 2):
            string[i], string[-1 * i - 1] = string[-1 * i - 1], string[i]
