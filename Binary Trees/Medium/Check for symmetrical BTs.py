# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def is_symmetric(self, root):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        # your code goes here
        if not root:
            return True

        def check(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.data != r2.data:
                return False
            return check(r1.left, r2.right) and check(r1.right, r2.left)

        return check(root.left, root.right)
