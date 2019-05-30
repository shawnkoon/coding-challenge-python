from .ListNode import ListNode


class Solution:
    """
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing
    together the nodes of the first two lists.
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(None)

        while l1 or l2:
            if not l1:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val < l1.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next

            cur = cur.next

        return head.next
