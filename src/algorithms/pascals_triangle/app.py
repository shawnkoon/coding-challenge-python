from typing import List


class PascalsTriangle:
    """
    Source : https://leetcode.com/problems/pascals-triangle/

    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Example:

        Input: 5
        Output:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]
    """

    def get_pascal(self, numRows: int) -> List[List[int]]:
        res = []

        if numRows <= 0:
            return res

        for row in range(numRows):
            cur = []
            for col in range(row + 1):
                if col == 0:
                    cur.append(1)
                elif col == row:
                    cur.append(1)
                else:
                    # middle
                    cur.append(res[row - 1][col - 1] + res[row - 1][col])
            res.append(cur)

        return res
