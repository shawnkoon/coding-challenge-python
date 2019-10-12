import unittest
from .app import AddTwoNumbers

from ...datastructures.ListNode import ListNode


class AddTwoNumbersTest(unittest.TestCase):
    def setUp(self):
        self.tester = AddTwoNumbers()

    def test_case_1(self):
        num1 = ListNode.from_list([2, 4, 3])
        num2 = ListNode.from_list([5, 6, 4])

        exp = ListNode.from_list([7, 0, 8])

        self.assertEqual(self.tester.function(num1, num2), exp)

    def test_case_2(self):
        num1 = ListNode.from_list([9])
        num2 = ListNode.from_list([8])

        exp = ListNode.from_list([7, 1])

        self.assertEqual(self.tester.function(num1, num2), exp)
