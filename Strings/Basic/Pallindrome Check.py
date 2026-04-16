class Solution:

    """
    T.C. : O(n)
    S.C. : O(1)
    """

    def palindromeCheck(self, s):
        # your code goes here
        return s == s[::-1]
