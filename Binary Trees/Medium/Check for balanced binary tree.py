# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        # Your code goes here
        def height(root):
            if not root:
                return 0
            leftHeight = height(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = height(root.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight-rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight)+1
        return height(root) != -1
