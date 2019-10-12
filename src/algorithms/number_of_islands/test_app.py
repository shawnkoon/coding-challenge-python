import unittest
from .app import NumberOfIslands
from typing import List


class NumberOfIslandsTest(unittest.TestCase):
    def setUp(self):
        self.tester = NumberOfIslands()

    def create_grid(self, s: str, limit: int) -> List[List[str]]:
        res = []

        for i in range(len(s) // limit):
            res.append(list(s[i * limit:(i + 1) * limit]))

        return res

    def test_case_1(self):
        grid = self.create_grid('11110110101100000000', 5)

        exp = 1

        self.assertEqual(self.tester.function(grid), exp)

    def test_case_2(self):
        grid = self.create_grid('11000110000010000011', 5)

        exp = 3

        self.assertEqual(self.tester.function(grid), exp)

    def test_case_3(self):
        grid = self.create_grid('111001111', 3)

        exp = 1

        self.assertEqual(self.tester.function(grid), exp)
