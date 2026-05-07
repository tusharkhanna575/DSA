class Solution:
    def kDistinctChar(self, s, k):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input string as we are iterating through all the characters of the string
        S.C. : O(k) as we are using a hashmap to store the count of the characters and the size of the hashmap will be at most k as we are only interested in k distinct characters
        """
        ans, n = 0, len(s)
        map = dict()
        l, r = 0, 0
        while r < n:
            map[s[r]] = map.get(s[r], 0)+1
            if (len(map) > k):
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    del map[s[l]]
                l += 1
            if len(map) <= k:
                ans = max(ans, r-l+1)
            r += 1
        return ans
