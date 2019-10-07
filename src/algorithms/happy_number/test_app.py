import unittest
from .app import HappyNumber


class HappyNumberTest(unittest.TestCase):
    def setUp(self):
        self.tester = HappyNumber()

    def test_case_1(self):
        n = 19
        self.assertTrue(self.tester.is_happy(n))

    def test_case_2(self):
        n = 97
        self.assertTrue(self.tester.is_happy(n))

    def test_case_3(self):
        n = 53
        self.assertFalse(self.tester.is_happy(n))
