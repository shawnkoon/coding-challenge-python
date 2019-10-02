from collections import deque
from .TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        cur = self.root

        # Edge Case
        if not cur:
            self.root = new_node

        while cur:
            if value < cur.value:
                if not cur.left:
                    cur.left = new_node
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = new_node
                    return
                cur = cur.right

    def lookup(self, value):
        cur = self.root

        while cur:
            if value == cur.value:
                return True

            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        return False

    def print_tree(self):
        queue = deque()

        if not self.root:
            return

        queue.append(self.root)

        while queue:
            node = queue.popleft()

            print(node.value, end=' ')

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    def remove(self, value):
        raise Exception('Not Implemented.')


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(170)
    bst.insert(15)
    bst.insert(1)

    bst.print_tree()

    print()

    print(bst.lookup(9))
    print(bst.lookup(30))
    print(bst.lookup(170))

    bst.remove(3)
