from typing import List


class SpiralMatrix:
    """
    Source : https://leetcode.com/problems/spiral-matrix/

    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

    Example 1:

    Input:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]

    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:

    Input:
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]

    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    """

    def function(self, matrix: List[List[int]]) -> List[int]:
        '''[N: N is total number of elements.] Time/Space O(N)'''
        flag = [[0] * len(l) for l in matrix]
        res = []
        i = j = 0

        if not matrix:
            return res

        res.append(matrix[i][j])
        flag[i][j] = 1

        while True:
            r = l = t = b = False

            # Right
            while j + 1 < len(matrix[i]) and flag[i][j + 1] == 0:
                r = True
                j += 1
                flag[i][j] = 1
                res.append(matrix[i][j])

            # Bottom
            while i + 1 < len(matrix) and flag[i + 1][j] == 0:
                b = True
                i += 1
                flag[i][j] = 1
                res.append(matrix[i][j])

            # Left
            while j - 1 >= 0 and flag[i][j - 1] == 0:
                l = True
                j -= 1
                flag[i][j] = 1
                res.append(matrix[i][j])

            # Top
            while i - 1 >= 0 and flag[i - 1][j] == 0:
                t = True
                i -= 1
                flag[i][j] = 1
                res.append(matrix[i][j])

            if not r and not l and not t and not b:
                break

        return res
