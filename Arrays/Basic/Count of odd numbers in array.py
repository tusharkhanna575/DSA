class Solution:

    """
    T.C. : O(n)
    S.C. : O(1)
    """

    def countOdd(self, arr, n):
        # Your code goes here
        ans = 0
        for i in arr:
            if i & 1:
                ans += 1
        return ans
