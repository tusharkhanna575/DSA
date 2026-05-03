class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        T.C. : O((log n) ^ 2) where n is the input number as we are iterating through all the bits of the number
        S.C. : O(1)"""
        # your code goes here
        if (dividend == divisor):
            return 1
        sign = True
        if ((dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0)):
            sign = False
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while (n >= d):
            cnt = 0
            while (n >= (d << (cnt+1))):
                cnt += 1
            ans += (1 << cnt)
            n -= (d*(1 << cnt))
        return ans if sign else -ans
