import unittest
from .app import ListPermutations


class ListPermutationsTest(unittest.TestCase):
    def setUp(self):
        self.tester = ListPermutations()

    def test_case_1(self):
        input_ = [1, 2, 3]
        exp = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        self.assertListEqual(self.tester.function(input_), exp)

    def test_case_2(self):
        input_ = [2, 3, 4, 5]
        exp = [
            [2, 3, 4, 5],
            [2, 3, 5, 4],
            [2, 4, 3, 5],
            [2, 4, 5, 3],
            [2, 5, 3, 4],
            [2, 5, 4, 3],
            [3, 2, 4, 5],
            [3, 2, 5, 4],
            [3, 4, 2, 5],
            [3, 4, 5, 2],
            [3, 5, 2, 4],
            [3, 5, 4, 2],
            [4, 2, 3, 5],
            [4, 2, 5, 3],
            [4, 3, 2, 5],
            [4, 3, 5, 2],
            [4, 5, 2, 3],
            [4, 5, 3, 2],
            [5, 2, 3, 4],
            [5, 2, 4, 3],
            [5, 3, 2, 4],
            [5, 3, 4, 2],
            [5, 4, 2, 3],
            [5, 4, 3, 2]
        ]
        self.assertListEqual(self.tester.function(input_), exp)
