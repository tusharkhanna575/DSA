# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def preorder(self, root):
        """
        Recursive way
        T.C. : O(n)
        S.C. : O(n)
        """
        # your code goes here
        if root == None:
            return self.ans
        self.ans.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.ans

    def preorderIterative(self, root):
        """
        Iterative way
        T.C. : O(n)
        S.C. : O(n)
        """
        ans = []
        st = [root]
        while st:
            node = st.pop()
            ans.append(node.data)

            if node.right:
                st.append(node.right)

            if node.left:
                st.append(node.left)

        return ans
