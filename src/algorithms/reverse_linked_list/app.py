from ...datastructures import ListNode


class ReverseLinkedList:
    """
    Source : https://leetcode.com/problems/reverse-linked-list/

    Reverse a singly linked list.

    Example:

        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL

    Follow up:

    A linked list can be reversed either iteratively or recursively. Could you implement both?
    """

    def reverse_iter(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next

        res = cur = ListNode(stack.pop())

        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next

        return res

    def reverse_rec(self, head: ListNode) -> ListNode:
        if not head:
            return None

        res = cur = ListNode(None)

        def helper(node: ListNode):
            nonlocal cur
            cur_node = ListNode(node.val)

            # Base Case
            if not node.next:
                cur.next = cur_node
                cur = cur.next
                return

            helper(node.next)

            cur.next = cur_node
            cur = cur.next

        helper(head)

        return res.next
