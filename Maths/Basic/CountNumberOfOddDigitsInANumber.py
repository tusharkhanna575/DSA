class Solution:
    def countOddDigit(self, n: int) -> int:
        ans = 0
        while n:
            digit = n % 10
            n //= 10
            if digit % 2 == 1:
                ans += 1

        return ans