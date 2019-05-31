from typing import List


class ValidateSudoku:
    """
    Source : https://leetcode.com/problems/valid-sudoku/

    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    """

    def function(self, board: List[List[str]]) -> bool:
        '''O(n)'''
        # Check each rows
        for row in board:
            h = {}
            for c in row:
                if c != '.' and h.get(c):
                    print('Row failed')
                    return False
                h[c] = 1

        # Check each columns
        for col in zip(*board):
            h = {}
            for c in col:
                if c != '.' and h.get(c):
                    print('Col failed')
                    return False
                h[c] = 1

        # Check 9 3x3s.
        for dy in range(3):
            for dx in range(3):
                h = {}
                start_x = 3 * dx
                start_y = 3 * dy

                for y in range(start_y, start_y + 3):
                    for x in range(start_x, start_x + 3):
                        c = board[x][y]
                        if c != '.' and h.get(c):
                            print('3x3 failed')
                            return False
                        h[c] = 1

        return True
