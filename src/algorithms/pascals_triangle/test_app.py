import unittest
from .app import PascalsTriangle


class PascalsTriangleTest(unittest.TestCase):
    def setUp(self):
        self.tester = PascalsTriangle()

    def test_case_1(self):
        payload = 1
        exp = [[1]]

        self.assertListEqual(self.tester.get_pascal(payload), exp)

    def test_case_2(self):
        payload = 5
        exp = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

        self.assertListEqual(self.tester.get_pascal(payload), exp)

    def test_case_3(self):
        payload = 7
        exp = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
               [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]

        self.assertListEqual(self.tester.get_pascal(payload), exp)
