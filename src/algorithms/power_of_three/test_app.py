import unittest
from .app import PowerOfThree


class PowerOfThreeTest(unittest.TestCase):
    def setUp(self):
        self.tester = PowerOfThree()

    def test_case_1(self):
        n = 27
        self.assertTrue(self.tester.is_power_of_three(n))

    def test_case_2(self):
        n = 0
        self.assertFalse(self.tester.is_power_of_three(n))

    def test_case_3(self):
        n = 9
        self.assertTrue(self.tester.is_power_of_three(n))

    def test_case_4(self):
        n = 45
        self.assertFalse(self.tester.is_power_of_three(n))
