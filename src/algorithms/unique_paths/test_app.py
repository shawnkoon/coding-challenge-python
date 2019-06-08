import unittest
from .app import UniquePaths


class UniquePathsTest(unittest.TestCase):
    def setUp(self):
        self.tester = UniquePaths()

    def test_case_1(self):
        m, n = 3, 2
        exp = 3
        self.assertEqual(self.tester.function(m, n), exp)

    def test_case_2(self):
        m, n = 7, 3
        exp = 28
        self.assertEqual(self.tester.function(m, n), exp)

    def test_case_3(self):
        m, n = 23, 12
        exp = 193536720
        self.assertEqual(self.tester.function(m, n), exp)
