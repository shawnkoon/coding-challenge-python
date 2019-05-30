class ListNode:
    '''Generic List Node object.'''

    def __init__(self, val):
        self.val = val
        self.next = None

    def __eq__(self, target):
        if self.val == target.val and self.next == target.next:
            return True
        return False
