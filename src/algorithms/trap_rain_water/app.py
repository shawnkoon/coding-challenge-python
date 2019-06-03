from typing import List


class TrapRainWater:
    """
    Source : https://leetcode.com/problems/trapping-rain-water/

    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    Example:

    3                               +
    2               +   #   #   #   +   +   #   +
    1       +   #   +   +   #   +   +   +   +   +   +

    + = bar
    # = water


    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    """

    def function(self, height: List[int]) -> int:
        '''
        O(n)
        Remember the rule: No matter how large an array is,
        max_water_height == min(left_bar, right_bar)
        '''

        l = tot = l_max = r_max = 0
        r = len(height) - 1

        while l < r:
            if height[l] <= height[r]:  # Leftside is shorter
                if height[l] > l_max:
                    l_max = height[l]
                tot += l_max - height[l]
                l += 1
            else:  # Rightside is shorter
                if height[r] > r_max:
                    r_max = height[r]
                tot += r_max - height[r]
                r -= 1

        return tot
