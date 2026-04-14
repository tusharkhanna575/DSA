class Solution:

    """
    T.C. : O(sqrt(n) * logn)
    S.C. : O(sqrt(n))
    """

    def divisors(self, n):
        ans = []
        chk = int(n**0.5)
        for i in range(1, chk+1):
            if n % i == 0:
                ans.append(i)
                if i != n//i:
                    ans.append(n//i)
        return sorted(ans)
