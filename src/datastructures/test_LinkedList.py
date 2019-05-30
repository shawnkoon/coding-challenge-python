import unittest
from .LinkedList import LinkedList
from .ListNode import ListNode


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.tester = LinkedList(ListNode(None))

    def test_case_1(self):
        exp = LinkedList(ListNode(None))
        self.assertEqual(self.tester, exp, '__eq__ should work')

    def test_case_2(self):
        self.tester.add_last(ListNode(2))
        self.tester.add_last(ListNode('shawn'))
        exp = LinkedList.from_arr([None, 2, 'shawn'])
        self.assertEqual(self.tester, exp, 'add_last() should work')

    def test_case_3(self):
        self.tester.add_first(ListNode(2))
        self.tester.add_first(ListNode('shawn'))
        exp = LinkedList.from_arr(['shawn', 2, None])
        self.assertEqual(self.tester, exp, 'add_first() should work')
