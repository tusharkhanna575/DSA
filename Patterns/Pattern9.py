"""
for n = 5, the pattern will be: 
    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    * 
"""


class Solution:

    """
    T.C. : O(n^2)
    S.C. : O(1)
    """

    def pattern9(self, n):
        for i in range(1, n + 1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))
        for i in range(n, 0, -1):
            print(" " * (n - i), end="")
            print("*" * (2 * i - 1))


if __name__ == "__main__":
    Solution().pattern9(5)
