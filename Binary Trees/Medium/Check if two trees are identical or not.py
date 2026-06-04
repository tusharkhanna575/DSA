# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        # your code goes here
        if p == None and q == None:
            return True

        elif p == None or q == None or p.data != q.data:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
