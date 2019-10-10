from ...datastructures.ListNode import ListNode


class LinkedListCycle:
    """
    Source : https://leetcode.com/problems/linked-list-cycle/

    Given a linked list, determine if it has a cycle in it.

    Example 1:

        Input: head = [3,2,0,-4]
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the second node.

    Example 2:

        Input: head = [1,2]
        Output: true
        Explanation: There is a cycle in the linked list, where tail connects to the first node.

    Example 3:

        Input: head = [1]
        Output: false
        Explanation: There is no cycle in the linked list.
    """

    def function(self, head: ListNode) -> bool:
        cur = head
        if not head or not head.next:
            return False

        runner = head.next

        while runner.next is not None and runner.next.next is not None:
            if runner is cur:
                return True

            cur = cur.next
            runner = runner.next.next

        return False
