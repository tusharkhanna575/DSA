class Solution:

    """
    T.C. : O(n)
    S.C. : O(n)
    """

    ans = 0

    def count_nodes(self, root):
        # your code goes here
        if root:
            self.ans += 1
            self.count_nodes(root.left)
            self.count_nodes(root.right)
        return self.ans
