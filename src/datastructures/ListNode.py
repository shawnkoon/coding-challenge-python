class ListNode:
    '''Generic List Node object.'''

    def __init__(self, val, next_: 'ListNode' = None):
        self.val = val
        self.next = next_

    def __eq__(self, target):
        if self.val == target.val and self.next == target.next:
            return True
        return False

    def __repr__(self):
        return f'ListNode(val={self.val}, next_={self.next})'


if __name__ == '__main__':
    temp = ListNode(123)
    temp2 = ListNode('shawnkoon', temp)

    print('temp =', temp)
    print('temp2 =', temp2)