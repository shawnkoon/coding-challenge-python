import unittest
from .app import ContainsDuplicate


class ContainsDuplicateTest(unittest.TestCase):
    def setUp(self):
        self.tester = ContainsDuplicate()

    def test_case_1(self):
        payload = [1, 2, 3, 1]
        self.assertTrue(self.tester.function(payload))

    def test_case_2(self):
        payload = [1, 2, 3, 4]
        self.assertFalse(self.tester.function(payload))

    def test_case_3(self):
        payload = [1, 2, 3, 1]
        self.assertTrue(self.tester.function(payload))
