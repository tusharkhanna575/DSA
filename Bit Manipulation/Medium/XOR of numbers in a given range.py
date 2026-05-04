class Solution:

    def XORtillN(self, n):
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n+1
        if n % 4 == 3:
            return 0
        return n

    def findRangeXOR(self, l, r):
        # your code goes here
        """
        T.C. : O(1)
        S.C. : O(1)
        """
        return self.XORtillN(l-1) ^ self.XORtillN(r)
