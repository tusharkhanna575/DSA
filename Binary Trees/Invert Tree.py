class Solution:

    """
    T.C. : O(n)
    S.C. : O(n)
    """

    def invert_tree(self, root):
        # your code goes here
        if root:
            root.left, root.right = root.right, root.left
            self.invert_tree(root.left)
            self.invert_tree(root.right)
        return root
