# Lib
from typing import List
from unittest import TestCase

# App
from .app import Solution
from .ListNode import ListNode


class MergeTwoSortedListsTest(TestCase):
    def setUp(self):
        self.tester = Solution()

    def convert_to_list_node(self, ara: List[int]) -> ListNode:
        head = cur = ListNode(None)

        for val in ara:
            cur.next = ListNode(val)
            cur = cur.next

        return head.next

    def convert_to_ara(self, list_node: ListNode) -> List[int]:
        res = []
        while list_node:
            res.append(list_node.val)
            list_node = list_node.next

        return res

    def test_case_1(self):
        ara_1: ListNode = self.convert_to_list_node([1, 2, 4])
        ara_2: ListNode = self.convert_to_list_node([1, 3, 4])
        res: List[int] = [1, 1, 2, 3, 4, 4]

        func_res = self.tester.mergeTwoLists(ara_1, ara_2)

        self.assertEqual(self.convert_to_ara(func_res), res)

    def test_case_2(self):
        ara_1: ListNode = self.convert_to_list_node([3, 5, 8])
        ara_2: ListNode = self.convert_to_list_node([1, 2, 7])
        res: List[int] = [1, 2, 3, 5, 7, 8]

        func_res = self.tester.mergeTwoLists(ara_1, ara_2)

        self.assertEqual(self.convert_to_ara(func_res), res)
