# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = []

    def inorder(self, root):
        """
        Recursive way
        T.C. : O(n)
        S.C. : O(n)
        """
        if root == None:
            return self.ans
        self.inorder(root.left)
        self.ans.append(root.data)
        self.inorder(root.right)
        return self.ans

    def inorderIterative(self, root):
        """
        Iterative way
        T.C. : O(n)
        S.C. : O(n)
        """
        ans = []
        st = []
        curr = root
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            node = st.pop()
            ans.append(node.data)
            curr = node.right
        return ans
