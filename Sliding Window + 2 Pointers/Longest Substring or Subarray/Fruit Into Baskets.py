class Solution:
    def totalFruits(self, fruits):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(3) as we are using a hashmap to store the count of the fruits and the size of the hashmap will be at most 3 as we are only interested in 2 types of fruits
        """
        n = len(fruits)
        ans, l, r = 0, 0, 0
        map = dict()

        while r < n:
            map[fruits[r]] = map.get(fruits[r], 0)+1
            if len(map) > 2:
                map[fruits[l]] -= 1
                if map[fruits[l]] == 0:
                    del map[fruits[l]]
                l += 1
            if len(map) <= 2:
                ans = max(ans, r-l+1)
            r += 1
        return ans
