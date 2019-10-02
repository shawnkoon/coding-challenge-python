import unittest
from .app import BubbleSort


class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.tester = BubbleSort()

    def test_case_1(self):
        numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
        exp = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]

        self.tester.sort(numbers)

        self.assertListEqual(numbers, exp)

    def test_case_2(self):
        numbers = [3, 2, 1]
        exp = [1, 2, 3]

        self.tester.sort(numbers)

        self.assertListEqual(numbers, exp)
