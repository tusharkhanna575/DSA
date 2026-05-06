class Solution:
    def longestNonRepeatingSubstring(self, s):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input string as we are iterating through all the characters of the string
        S.C. : O(256) 
        """
        n = len(s)
        ans = 0
        l, r = 0, 0
        hash = [-1]*256

        while r < n:
            if hash[ord(s[r])] != -1:
                l = max(hash[ord(s[r])]+1, l)
            curr = r-l+1
            ans = max(ans, curr)
            hash[ord(s[r])] = r
            r += 1
        return ans
