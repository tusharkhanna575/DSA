class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # your code goes here
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        l, r, maxLen, maxFreq = 0, 0, 0, 0
        n = len(s)
        hash = [0]*26
        while r < n:
            hash[ord(s[r])-ord('A')] += 1
            maxFreq = max(maxFreq, hash[ord(s[r])-ord('A')])
            if ((r-l+1)-maxFreq) > k:
                hash[ord(s[l])-ord('A')] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen
