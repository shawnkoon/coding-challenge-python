class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'TreeNode({self.value})'


if __name__ == '__main__':
    print('I am TreeNode class.')
