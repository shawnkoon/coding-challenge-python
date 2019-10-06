import unittest
from .app import ReverseLinkedList

from ...datastructures.ListNode import ListNode


class ReverseLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.tester = ReverseLinkedList()

    def test_case_1(self):
        payload = ListNode.from_list([1, 2, 3, 4, 5])
        exp = ListNode.from_list([5, 4, 3, 2, 1])

        self.assertEqual(self.tester.reverse_iter(
            payload), exp, 'Iterative Solution.')
        self.assertEqual(self.tester.reverse_rec(
            payload), exp, 'Recursive Solution.')
