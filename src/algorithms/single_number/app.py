from typing import List


class SingleNumber:
    """
    Source : https://leetcode.com/problems/single-number/

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1
    Example 2:

    Input: [4,1,2,1,2]
    Output: 4
    """

    def singleNumber(self, nums: List[int]) -> int:
        hash_set = set()

        for n in nums:
            if n in hash_set:
                hash_set.remove(n)
            else:
                hash_set.add(n)

        return hash_set.pop()
