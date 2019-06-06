import unittest
from .app import ListJumpGame


class ListJumpGameTest(unittest.TestCase):
    def setUp(self):
        self.tester = ListJumpGame()

    def test_case_1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertTrue(self.tester.function(nums), 'function')
        self.assertTrue(self.tester.function2(nums), 'function2')

    def test_case_2(self):
        nums = [3, 2, 1, 0, 4]
        self.assertFalse(self.tester.function(nums), 'function')
        self.assertFalse(self.tester.function2(nums), 'function2')

    def test_case_3(self):
        nums = [3, 0, 8, 2, 0, 0, 1]
        self.assertTrue(self.tester.function(nums), 'function')
        self.assertTrue(self.tester.function2(nums), 'function2')
