class Solution:
    def isPrime(self, n):
        #your code goes here
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def primeUptoN(self, n):
        ans = 0
        for i in range(2, n + 1):
            if self.isPrime(i):
                ans += 1
        return ans