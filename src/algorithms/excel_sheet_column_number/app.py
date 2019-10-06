class ExcelColumnNumber:
    """
    Source : https://leetcode.com/problems/excel-sheet-column-number/

    Given a column title as appear in an Excel sheet, return its corresponding column number.

    For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...

    Example 1:
        Input: "A"
        Output: 1
    Example 2:
        Input: "AB"
        Output: 28
    Example 3:
        Input: "ZY"
        Output: 701
    """

    def get_number(self, s: int) -> int:
        '''
        Think of them as base 26 number system.
        '''
        columns = {k: i + 1 for i, k in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                                                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}
        base = 26
        tot = 0

        for i in range(len(s)):
            rev_index = -1 * i - 1
            tot += columns[s[rev_index]] * (base ** i)

        return tot
