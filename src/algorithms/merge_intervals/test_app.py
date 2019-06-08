import unittest
from .app import MergeIntervals


class MergeIntervalsTest(unittest.TestCase):
    def setUp(self):
        self.tester = MergeIntervals()

    def test_case_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        exp = [[1, 6], [8, 10], [15, 18]]
        self.assertListEqual(self.tester.function(intervals), exp, 'function')
        self.assertListEqual(self.tester.function2(
            intervals), exp, 'function2')

    def test_case_2(self):
        intervals = [[1, 4], [4, 5]]
        exp = [[1, 5]]
        self.assertListEqual(self.tester.function(intervals), exp, 'function')
        self.assertListEqual(self.tester.function2(
            intervals), exp, 'function2')

    def test_case_3(self):
        intervals = [[1, 4], [0, 4]]
        exp = [[0, 4]]
        self.assertListEqual(self.tester.function(intervals), exp, 'function')
        self.assertListEqual(self.tester.function2(
            intervals), exp, 'function2')

    def test_case_4(self):
        intervals = [[1, 4], [0, 0]]
        exp = [[0, 0], [1, 4]]
        self.assertListEqual(self.tester.function(intervals), exp, 'function')
        self.assertListEqual(self.tester.function2(
            intervals), exp, 'function2')

    def test_case_5(self):
        intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
        exp = [[1, 10]]
        self.assertListEqual(self.tester.function(intervals), exp, 'function')
        self.assertListEqual(self.tester.function2(
            intervals), exp, 'function2')
