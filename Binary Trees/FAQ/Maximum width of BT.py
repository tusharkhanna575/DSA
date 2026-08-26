# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        #your code goes here
        """
        T.C. : O(n)
        S.C. : O(n)
        """
        if not root:
            return 0

        ans=0
        q=deque([(root,0)])

        while q:
            n=len(q)
            mini=q[0][1]
            l=r=0

            for i in range(n):
                curr=q[0][1]-mini
                node=q[0][0]
                q.popleft()

                if i==0:
                    l=curr
                if i==n-1:
                    r=curr
                
                if node.left:
                    q.append((node.left,curr*2+1))
                if node.right:
                    q.append((node.right,curr*2+2))
                
                ans=max(ans,r-l+1)
        
        return ans