import unittest
from .app import HouseRobber


class HouseRobberTest(unittest.TestCase):
    def setUp(self):
        self.tester = HouseRobber()

    def test_case_1(self):
        payload = [1, 2, 3, 1]
        exp = 4
        self.assertEquals(self.tester.function(payload), exp)

    def test_case_2(self):
        payload = [2, 7, 9, 3, 1]
        exp = 12
        self.assertEquals(self.tester.function(payload), exp)
