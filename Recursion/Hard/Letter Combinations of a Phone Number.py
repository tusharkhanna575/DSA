class Solution:

    def letterCombinations(self, digits):
        """
        T.C. : O(4^n * n)
        S.C. : O(n)
        """
        # your code goes here

        def help(digits, ans, idx, curr):
            if idx == len(digits):
                ans.append(curr)
                return
            s = map[int(digits[idx])]
            for i in s:
                help(digits, ans, idx+1, curr+i)

        map = ['', '', 'abc', 'def', 'ghi',
               'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []
        if not digits:
            return ans
        help(digits, ans, 0, '')
        return ans
