class Solution:

    """
    T.C. : O(1)
    S.C. : O(1)
    """

    def countDigit(self, n: int) -> int:
        ans = 1
        while n >= 9:
            n //= 10
            ans += 1
        return ans
