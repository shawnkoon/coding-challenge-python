class Solution:
    """
    Source : https://leetcode.com/problems/palindrome-number/
    Determine whether an integer is a palindrome.
    An integer is a palindrome when it reads the same backward as forward.
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if str(x) == str(x)[::-1]:
            return True

        return False

    def isPalindrome_int(self, x: int) -> bool:
        """Algorithm without using str"""
        if x < 0:
            return False

        initial: int = x
        reverse: int = x % 10
        x //= 10

        while x > 0:
            pop = x % 10
            reverse = reverse * 10 + pop
            x //= 10

        return True if reverse == initial else False
