class Solution:

    """
    T.C. : O(sqrt(n))
    S.C. : O(1)
    """

    def isPrime(self, n):
        # your code goes here
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
