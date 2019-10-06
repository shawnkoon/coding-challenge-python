import unittest
from .app import FirstUniqueCharacter


class FirstUniqueCharacterTest(unittest.TestCase):
    def setUp(self):
        self.tester = FirstUniqueCharacter()

    def test_case_1(self):
        s = "hello"
        exp = 0
        self.assertEqual(self.tester.first_unique_char(s), exp)

    def test_case_2(self):
        s = "mynameisshawnkoonyes"
        exp = 6
        self.assertEqual(self.tester.first_unique_char(s), exp)
