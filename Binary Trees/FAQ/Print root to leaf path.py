# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def allRootToLeaf(self, root):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        #your code goes here
        path,ans=[],[]

        def dfs(root):
            if not root:
                return
            path.append(root.data)
            if not root.left and not root.right:
                ans.append(path.copy())
            else:
                dfs(root.left)
                dfs(root.right)
            path.pop()
        
        dfs(root)
        return ans