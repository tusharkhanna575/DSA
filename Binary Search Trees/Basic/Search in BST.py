# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, val):
        #your code goes here
        """
        T.C. : O(height of tree)
        S.C. : O(1)
        """
        while root:
            if root.data == val:
                return root
            elif root.data > val:
                root = root.left
            elif root.data < val:
                root = root.right
        return None