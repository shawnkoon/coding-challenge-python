from unittest import TestCase
from .app import Solution


class ValidParentheses(TestCase):
    def setUp(self):
        self.tester = Solution()

    def test_case_1(self):
        input_str = "({[]})"
        output = True
        self.assertEqual(self.tester.isValid(input_str), output)

    def test_case_2(self):
        input_str = "()[]{}"
        output = True
        self.assertEqual(self.tester.isValid(input_str), output)

    def test_case_3(self):
        input_str = "("
        output = False
        self.assertEqual(self.tester.isValid(input_str), output)

    def test_case_4(self):
        input_str = "([)]"
        output = False
        self.assertEqual(self.tester.isValid(input_str), output)
