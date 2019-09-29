import unittest
from .app import RotateArray


class RotateArrayTest(unittest.TestCase):
    def setUp(self):
        self.tester = RotateArray()

    def test_case_1(self):
        payload = [1, 2, 3], 4
        exp = [3, 1, 2]
        self.tester.function(*payload)
        self.assertListEqual(payload[0], exp)

    def test_case_2(self):
        payload = [1, 2, 3, 4, 5, 6, 7], 3
        exp = [5, 6, 7, 1, 2, 3, 4]
        self.tester.function(*payload)
        self.assertListEqual(payload[0], exp)

    def test_case_3(self):
        payload = [1, 2], 3
        exp = [2, 1]
        self.tester.function(*payload)
        self.assertListEqual(payload[0], exp)

    def test_case_4(self):
        payload = [-1], 2
        exp = [-1]
        self.tester.function(*payload)
        self.assertListEqual(payload[0], exp)
