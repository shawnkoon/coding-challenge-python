import unittest
from .app import ValidAnagram


class ValidAnagramTest(unittest.TestCase):
    def setUp(self):
        self.tester = ValidAnagram()

    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.tester.is_anagram(s, t))

    def test_case_2(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.tester.is_anagram(s, t))
