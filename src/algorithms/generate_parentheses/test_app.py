import unittest
from .app import ParenthesesGenerator


class ParenthesesGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.tester = ParenthesesGenerator()

    def test_case_1(self):
        input_ = 3
        exp = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertListEqual(self.tester.function(input_), exp)
