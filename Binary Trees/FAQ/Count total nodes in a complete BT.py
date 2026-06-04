class Solution:
    ans = 0

    def count_nodes(self, root):
        """
        T.C. : O(n)
        S.C. : O(height of tree)
        """
        # your code goes here
        if root:
            self.ans += 1
            self.count_nodes(root.left)
            self.count_nodes(root.right)
        return self.ans
