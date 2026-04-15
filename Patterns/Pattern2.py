"""
for n = 5, the pattern will be:
*
**
***
****
*****
"""


class Solution:

    """
    T.C. : O(n^2)
    S.C. : O(1)
    """

    def pattern2(self, n):
        for i in range(1, n+1):
            print("*"*i)
