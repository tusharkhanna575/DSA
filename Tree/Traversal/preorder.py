class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder_traversal(root):
    res = []
    if root:
        res.append(root.val)
        res += preorder_traversal(root.left)
        res += preorder_traversal(root.right)
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

    print("Preorder Traversal of the tree is:", preorder_traversal(root))