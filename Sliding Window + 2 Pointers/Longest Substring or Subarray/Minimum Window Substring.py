class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # your code goes here
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        hash = [0]*256
        n, m = len(s), len(t)
        idx = -1
        minLen = float('inf')
        for i in t:
            hash[ord(i)] += 1
        cnt, l, r = 0, 0, 0
        while r < n:
            if hash[ord(s[r])] > 0:
                cnt += 1
            hash[ord(s[r])] -= 1
            while cnt == m:
                if ((r-l+1) < minLen):
                    minLen = r-l+1
                    idx = l
                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    cnt -= 1
                l += 1
            r += 1
        return s[idx:idx+minLen] if idx != -1 else ""
