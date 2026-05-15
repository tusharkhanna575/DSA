# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.In = []
        self.pre = []
        self.post = []

    def inOrder(self, root):
        if root == None:
            return self.In
        self.inOrder(root.left)
        self.In.append(root.data)
        self.inOrder(root.right)
        return self.In

    def preOrder(self, root):
        if root == None:
            return self.pre
        self.pre.append(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)
        return self.pre

    def postOrder(self, root):
        if root == None:
            return self.post
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.post.append(root.data)
        return self.post

    def tree_traversal(self, root):
        # your code goes here
        """
        T.C. : O(3*n)
        S.C. : O(3*n)
        """
        ans = [self.inOrder(root), self.preOrder(root), self.postOrder(root)]
        return ans
