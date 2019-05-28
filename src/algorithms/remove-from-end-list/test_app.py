from typing import List
import unittest
from .app import RemoveFromNthEndLinkedList, ListNode


class RemoveFromNthEndLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.tester = RemoveFromNthEndLinkedList()

    def createListNode(self, input_list: List[int]) -> ListNode:
        res = cur = ListNode(None)
        for i in input_list:
            cur.next = ListNode(i)
            cur = cur.next

        return res.next

    def getList(self, head: ListNode) -> List[int]:
        cur = head
        res = []
        while cur:
            res.append(cur.value)
            cur = cur.next

        return res

    def test_case_1(self):
        input_head = self.createListNode([1, 2])
        n = 2
        output_head = self.createListNode([2])

        self.assertListEqual(
            self.getList(self.tester.removeNthFromEnd(input_head, n)),
            self.getList(output_head)
        )

    def test_case_2(self):
        input_head = self.createListNode([1, 2, 3, 4, 5])
        n = 2
        output_head = self.createListNode([1, 2, 3, 5])

        self.assertListEqual(
            self.getList(self.tester.removeNthFromEnd(input_head, n)),
            self.getList(output_head)
        )
