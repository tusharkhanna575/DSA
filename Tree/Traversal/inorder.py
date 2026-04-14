class TreeNode:

    """
    T.C. : O(n)
    S.C. : O(n)
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder_traversal(root):
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root.val)
        res = res + inorder_traversal(root.right)
    return res


if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left = TreeNode(0)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(0.5)

    print("Inorder Traversal of the tree is:", inorder_traversal(root))
