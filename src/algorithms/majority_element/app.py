from typing import List


class MajorityElement:
    """
    Source : https://leetcode.com/problems/majority-element/

    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.

    Example 1:

        Input: [3,2,3]
        Output: 3
    Example 2:

        Input: [2,2,1,1,1,2,2]
        Output: 2
    """

    def find_majority_element(self, nums: List[int]) -> int:
        count_ht = {}

        max_count = len(nums) // 2

        if max_count == 0:
            return nums[0]

        for n in nums:
            count = count_ht.get(n)

            if count is None:
                count_ht[n] = 1
            else:
                if count >= max_count:
                    return n

                count_ht[n] += 1

        return
