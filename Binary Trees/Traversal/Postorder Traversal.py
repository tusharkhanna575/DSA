# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def postorder(self, root):
        # your code goes here
        """
        Recursive way
        T.C. : O(n)
        S.C. : O(n)
        """
        if root == None:
            return self.ans
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.data)
        return self.ans

    def postorderIterative(self, root):
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

            if node.left:
                st.append(node.left)

            if node.right:
                st.append(node.right)

        return ans[::-1]
