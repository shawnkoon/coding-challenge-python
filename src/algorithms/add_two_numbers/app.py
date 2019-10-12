from ...datastructures.ListNode import ListNode


class AddTwoNumbers:
    """
    Source : https://leetcode.com/problems/add-two-numbers/

    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:

        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
    """

    def function(self, num1: ListNode, num2: ListNode) -> ListNode:
        res = cur = ListNode(None)
        power = 0

        while num1 or num2:
            if not num1:
                power, r = divmod(num2.val + power, 10)
                cur.next = ListNode(r)

                num2 = num2.next
                cur = cur.next
                continue

            if not num2:
                power, r = divmod(num1.val + power, 10)
                cur.next = ListNode(r)

                num1 = num1.next
                cur = cur.next
                continue

            power, r = divmod(num1.val + num2.val + power, 10)

            cur.next = ListNode(r)

            cur = cur.next
            num1 = num1.next
            num2 = num2.next

        if power:
            cur.next = ListNode(power)

        return res.next
