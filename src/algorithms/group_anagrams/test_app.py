import unittest
from .app import GroupAnagrams


class GroupAnagramsTest(unittest.TestCase):
    def setUp(self):
        self.tester = GroupAnagrams()

    def test_case_1(self):
        input_ = ["eat", "tea", "tan", "ate", "nat", "bat"]
        exp = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertListEqual(self.tester.function(input_), exp)
