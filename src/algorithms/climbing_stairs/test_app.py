import unittest
from .app import ClimbingStairs


class ClimbingStairsTest(unittest.TestCase):
    def setUp(self):
        self.tester = ClimbingStairs()

    def test_case_1(self):
        payload = 0
        exp = 0
        self.assertEqual(self.tester.function(payload), exp)

    def test_case_2(self):
        payload = 3
        exp = 3
        self.assertEqual(self.tester.function(payload), exp)

    def test_case_3(self):
        payload = 15
        exp = 987
        self.assertEqual(self.tester.function(payload), exp)
