"""
for n = 5, the pattern will be:

12345
1234
123
12
1
"""


class Solution:

    """
    T.C. : O(n^2)
    S.C. : O(1)
    """

    def pattern6(self, n):
        for i in range(n, -1, -1):
            for j in range(1, i + 1):
                print(j, end="")
            print()
