class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # your code goes here
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        last_seen = [-1]*3
        cnt = 0
        for i in range(len(s)):
            last_seen[ord(s[i])-ord('a')] = i
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                cnt += (1+min(last_seen))
        return cnt
