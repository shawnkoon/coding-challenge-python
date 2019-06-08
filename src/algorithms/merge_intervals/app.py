from typing import List


class MergeIntervals:
    """
    Source : https://leetcode.com/problems/merge-intervals/

    Given a collection of intervals, merge all overlapping intervals.

    # Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]

    Output: [[1,6],[8,10],[15,18]]

    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    # Example 2:

    Input: [[1,4],[4,5]]

    Output: [[1,5]]

    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """

    def function(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0

        intervals.sort(key=lambda x: x[0])

        while i < len(intervals):
            left, right = intervals[i]

            # check next
            while i + 1 < len(intervals):
                n_left, n_right = intervals[i + 1]
                if n_left <= right:
                    right = max(right, n_right)
                    i += 1
                else:
                    break

            res.append([left, right])
            i += 1

        return res

    def function2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])

        return res
