import unittest
from typing import List

from .app import MergeKSortedLinkedLists, ListNode


class MergeKSortedLinkedListsTest(unittest.TestCase):
    @staticmethod
    def build_linked_list(arr: List[int]) -> ListNode:
        head = cur = ListNode(None)

        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next

        return head.next

    @staticmethod
    def destory_linked_list(ll: ListNode) -> List[int]:
        res = []

        while ll:
            res.append(ll.val)
            ll = ll.next

        return res

    def setUp(self):
        self.tester = MergeKSortedLinkedLists()

    def test_case_1(self):
        input_ = [
            self.build_linked_list([1, 4, 5]),
            self.build_linked_list([1, 3, 4]),
            self.build_linked_list([2, 6])
        ]
        output = self.tester.mergeKLists(input_)
        exp = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertListEqual(self.destory_linked_list(output), exp)
