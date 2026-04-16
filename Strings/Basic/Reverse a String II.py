class Solution:

    """
    T.C. : O(n)
    S.C. : O(1)
    """

    def reverseString(self, s):
        # your code goes here
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
