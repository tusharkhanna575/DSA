class Solution:

    """
    T.C. : O(log n)
    S.C. : O(log n)
    """

    def myPow(self, x: float, n: int) -> float:
        # your code goes here
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n//2)
