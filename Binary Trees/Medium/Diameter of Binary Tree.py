# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        # your code goes here
        self.diameter = 0

        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            self.diameter = max(self.diameter, lh+rh)
            return 1+max(lh, rh)

        height(root)
        return self.diameter
