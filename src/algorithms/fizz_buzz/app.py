from typing import List


class FizzBuzz:
    """
    Source : https://leetcode.com/problems/fizz-buzz/

    Write a program that outputs the string representation of numbers from 1 to n.

    But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

    Example:

    n = 15,

    Return:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    """

    def fizzBuzz(self, num: int) -> List[str]:
        res = []

        for n in range(1, num + 1):
            is_mod_3 = n % 3 == 0
            is_mod_5 = n % 5 == 0

            if is_mod_3 and is_mod_5:
                res.append('FizzBuzz')
            elif is_mod_3:
                res.append('Fizz')
            elif is_mod_5:
                res.append('Buzz')
            else:
                res.append(str(n))

        return res
