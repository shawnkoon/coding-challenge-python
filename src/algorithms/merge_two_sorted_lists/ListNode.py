from typing import Optional


class ListNode:
    """
    List node to be used for this problem.
    """

    def __init__(self, x: Optional[int]):
        self.val: int = x
        self.next: ListNode = None
