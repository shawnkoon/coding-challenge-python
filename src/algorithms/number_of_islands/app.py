from typing import List


class NumberOfIslands:
    """
    Source : https://leetcode.com/problems/number-of-islands/

    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Example 1:

        Input:
        11110
        11010
        11000
        00000

        Output: 1
    Example 2:

        Input:
        11000
        11000
        00100
        00011

        Output: 3
    """

    def function(self, grid: List[List[str]]) -> int:
        island_coords = set()
        count = 0

        def depth_first_search(i, j):
            if (i, j) in island_coords:
                return

            island_coords.add((i, j))

            if i + 1 < len(grid) and grid[i + 1][j] != "0":
                depth_first_search(i + 1, j)

            if j + 1 < len(grid[i]) and grid[i][j + 1] != "0":
                depth_first_search(i, j + 1)

            if i - 1 >= 0 and grid[i - 1][j] != "0":
                depth_first_search(i - 1, j)

            if j - 1 >= 0 and grid[i][j - 1] != "0":
                depth_first_search(i, j - 1)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if (i, j) in island_coords or cell == "0":
                    continue

                count += 1
                depth_first_search(i, j)

        return count
