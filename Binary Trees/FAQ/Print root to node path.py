# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:

    def rootToNodePath(self, root, target):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        #your code goes here
        path=[]
        
        def dfs(root):
            if not root:
                return False
            path.append(root.data)
            if root.data==target:
                return True
            if dfs(root.left) or dfs(root.right):
                return True
            path.pop()
            return False
        
        dfs(root)
        return path