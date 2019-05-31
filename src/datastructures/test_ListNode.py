import unittest
from .ListNode import ListNode


class ListNodeTest(unittest.TestCase):
    def test_case_1(self):
        val = 'shawnkoon'
        new_list_node = ListNode(val)
        self.assertEqual(new_list_node.val, val, 'Value should be assigned')
        self.assertEqual(new_list_node.next, None,
                         'Next should be null by default')

    def test_case_2(self):
        val = 1234
        dummy_node = ListNode(None)
        new_list_node = ListNode(val)
        new_list_node.next = dummy_node

        self.assertEqual(new_list_node.val, val, 'Value should be assigned')
        self.assertEqual(new_list_node.next, dummy_node,
                         'Should be able to assign next value')

    def test_case_3(self):
        self.assertEqual(ListNode(123), ListNode(123), '__eq__ should work')
