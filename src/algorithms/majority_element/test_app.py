import unittest
from .app import MajorityElement


class MajorityElementTest(unittest.TestCase):
    def setUp(self):
        self.tester = MajorityElement()

    def test_case_1(self):
        payload = [1]
        exp = 1
        self.assertEqual(self.tester.find_majority_element(payload), exp)

    def test_case_2(self):
        payload = [3, 2, 3]
        exp = 3
        self.assertEqual(self.tester.find_majority_element(payload), exp)

    def test_case_3(self):
        payload = [2, 2, 1, 1, 1, 2, 2]
        exp = 2
        self.assertEqual(self.tester.find_majority_element(payload), exp)
