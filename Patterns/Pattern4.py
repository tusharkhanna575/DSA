"""
for n = 5, the pattern will be:

1
22
333
4444
55555
"""


class Solution:

    """
    T.C. : O(n^2)
    S.C. : O(1)
    """

    def pattern4(self, n):
        for i in range(1, n + 1):
            print(str(i) * i, end="")
            print()
