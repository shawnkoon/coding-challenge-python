from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeKSortedLinkedLists:
    """
    Source : https://leetcode.com/problems/merge-k-sorted-lists/

    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

    Example:

    Input:
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    Output: 1->1->2->3->4->4->5->6
    """

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        tot = []
        head = cur = ListNode(None)

        for list_item in lists:
            while list_item:
                tot.append(list_item.val)
                list_item = list_item.next

        for i in sorted(tot):
            cur.next = ListNode(i)
            cur = cur.next

        return head.next
