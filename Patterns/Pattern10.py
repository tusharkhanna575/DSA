"""
for n = 5, the pattern will be:
*
**
***
****
*****
****
***
**
*
"""


class Solution:

    """
    T.C. : O(n^2)
    S.C. : O(1)
    """

    def pattern10(self, n):
        for i in range(1, n+1):
            print("*"*i)
        for i in range(n-1, 0, -1):
            print("*"*i)


if __name__ == "__main__":
    Solution().pattern10(5)
