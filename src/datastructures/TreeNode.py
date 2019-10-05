from typing import List


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


if __name__ == '__main__':
    print('I am TreeNode class.')
