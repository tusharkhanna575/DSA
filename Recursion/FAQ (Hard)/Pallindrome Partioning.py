class Solution:
    def partition(self, s: str):
        """
        T.C. : O(n * 2^n)
        S.C. : O(n)
        """
        # your code goes here

        def isPallindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(idx, path):
            if idx == len(s):
                res.append(path[:])
                return
            for i in range(idx, len(s)):
                if isPallindrome(idx, i):
                    path.append(s[idx:i+1])
                    dfs(i+1, path)
                    path.pop()

        res = []
        dfs(0, [])
        return res
