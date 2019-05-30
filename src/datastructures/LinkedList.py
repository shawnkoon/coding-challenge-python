from typing import List
from .ListNode import ListNode


class LinkedList:
    '''LinkedList object which composes ListNode objects'''

    def __init__(self, head: ListNode):
        if not head:
            raise TypeError("head can not be None.")
        self.head = head
        self.size = 1

    def __eq__(self, target: 'LinkedList'):
        if self.size == target.size and self.head == target.head:
            return True
        return False

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __repr__(self):
        return f"LinkedList(head=ListNode({[c.val for c in self]}))"

    @classmethod
    def from_arr(cls: 'LinkedList', values: List):
        if len(values) == 0:
            raise ValueError("values can not be empty.")

        res = cls(ListNode(values[0]))
        cur = res.head
        for i in range(1, len(values)):
            cur.next = ListNode(values[i])
            cur = cur.next
            res.size += 1

        return res

    def add_last(self, node: ListNode):
        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = node
        self.size += 1

    def add_first(self, node: ListNode):
        node.next = self.head
        self.head = node
        self.size += 1


if __name__ == '__main__':
    temp = LinkedList.from_arr([1, 2, 3])
    temp2 = LinkedList(ListNode(1))
    temp2.add_last(ListNode(2))
    temp2.add_last(ListNode(3))

    print('temp =', temp, hex(id(temp)))
    print('temp2 =', temp2, hex(id(temp2)))
    print('temp == temp2', temp == temp2)
