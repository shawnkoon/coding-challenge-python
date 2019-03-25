from typing import List


class ReverseInteger:
    """
    Source: https://leetcode.com/problems/reverse-integer/
    Given a 32-bit signed integer, reverse digits of an integer.
    """

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        res_sign: int = -1 if x < 0 else 1
        res_reversed: List[int] = []

        x = x // res_sign

        while x > 0:
            res_reversed.append(x % 10)
            x = x // 10

        result = res_sign * int(''.join(map(str, res_reversed)))

        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0

        return result
