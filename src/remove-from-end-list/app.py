class ListNode:
    '''Helper Singly LinkedList'''

    def __init__(self, x):
        self.value = x
        self.next = None


class RemoveFromNthEndLinkedList:
    """
    Source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = cur = runner = ListNode(None)
        root.next = head

        for _ in range(n):
            runner = runner.next

        while runner.next:
            cur = cur.next
            runner = runner.next

        cur.next = cur.next.next

        return root.next
