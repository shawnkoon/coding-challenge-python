from typing import List
from collections import deque


class TreeNode:
    @classmethod
    def from_list(cls, ara: List[int]):
        if not ara:
            return None

        def build_tree(index: int):
            if index >= len(ara):
                return None

            if ara[index] is None:
                return None

            root = cls(ara[index])

            root.left = build_tree(index * 2 + 1)

            root.right = build_tree(index * 2 + 2)

            return root

        return build_tree(0)

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'TreeNode({self.value})'

    def to_list(self):
        res = []
        queue = deque()

        queue.append(self)

        while queue:
            cur = queue.popleft()

            if cur is None:
                res.append(None)
                continue

            res.append(cur.value)

            if not cur.left and not cur.right:
                continue

            queue.append(cur.left)
            queue.append(cur.right)

        return res if res[-1] is not None else res[:-1]


if __name__ == '__main__':
    print('I am TreeNode class.')
