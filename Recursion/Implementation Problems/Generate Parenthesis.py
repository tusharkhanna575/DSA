from typing import List


class Solution:

    """
    T.C. : O(4^n / sqrt(n))
    S.C. : O(4^n / sqrt(n))
    """

    def generateParenthesis(self, n: int) -> List[str]:
        """
        To generate all combinations of length 2*n, we can use backtracking. We will keep track of the number of open and close parentheses used so far. We can only add an open parenthesis if we have not used all n open parentheses, and we can only add a close parenthesis if it does not exceed the number of open parentheses used. When we have used all n open and n close parentheses, we can add the current combination to our answer list.
        """
        # your code goes here
        ans = []

        def generate(open: int, close: int, n: int, curr: str, ans: List[str]) -> None:
            if open == close == n:
                ans.append(curr)
                return

            if open < n:
                generate(open+1, close, n, curr+'(', ans)

            if close < open:
                generate(open, close+1, n, curr+')', ans)

        generate(0, 0, n, '', ans)
        return ans
