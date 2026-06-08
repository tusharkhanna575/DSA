# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def boundary(self, root):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        # your code goes here

        def isLeafNode(root):
            return not root.right and not root.left

        def leftBoundary(root, ans):
            curr = root.left
            while curr:
                if not isLeafNode(curr):
                    ans.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right

        def rightBoundary(root, ans):
            curr = root.right
            temp = []
            while curr:
                if not isLeafNode(curr):
                    temp.append(curr.data)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            ans.extend(temp[::-1])

        def leafBoundary(root, ans):
            if isLeafNode(root):
                ans.append(root.data)
                return
            if root.left:
                leafBoundary(root.left, ans)
            if root.right:
                leafBoundary(root.right, ans)

        ans = []
        if not root:
            return ans
        if not isLeafNode(root):
            ans.append(root.data)

        leftBoundary(root, ans)
        leafBoundary(root, ans)
        rightBoundary(root, ans)

        return ans
