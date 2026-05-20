# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        # your code goes here
        """
        Recursive way
        T.C. : O(n)
        S.C. : O(n)
        """
        if root == None:
            return 0

        max_right = self.maxDepth(root.right)
        max_left = self.maxDepth(root.left)

        return (max(max_left, max_right) + 1)

    def maxDepthIterative(self, root):
        """
        Iterative way
        T.C. : O(n)
        S.C. : O(n)
        """
        if root == None:
            return 0

        q = [root]
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return depth
