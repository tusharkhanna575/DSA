"""
for n = 5, the pattern will be:

1
12
123
1234
12345
"""


class Solution:

    """
    T.C. : O(n^2)
    S.C. : O(1)
    """

    def pattern3(self, n):
        for j in range(1, n + 1):
            for i in range(1, j + 1):
                print(i, end="")
            print()
