class ValidatePalindrome:
    """
    Source : https://leetcode.com/problems/valid-palindrome/

    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

        Input: "A man, a plan, a canal: Panama"
        Output: true
    Example 2:

        Input: "race a car"
        Output: false
    """

    def function(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1

        while lo <= hi:
            if not s[lo].isalpha() and not s[lo].isdigit():
                lo += 1
                continue

            if not s[hi].isalpha() and not s[hi].isdigit():
                hi -= 1
                continue

            if s[lo].lower() != s[hi].lower():
                return False

            lo += 1
            hi -= 1

        return True
