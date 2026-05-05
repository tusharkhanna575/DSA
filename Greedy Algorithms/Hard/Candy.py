class Solution:
    def candy(self, ratings):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1)"""
        n = len(ratings)
        sum, i = 1, 1
        while (i < n):
            if ratings[i] == ratings[i-1]:
                sum += 1
                i += 1
                continue
            peak = 1
            while (i < n and ratings[i] > ratings[i-1]):
                peak += 1
                sum += peak
                i += 1
            down = 1
            while (i < n and ratings[i] < ratings[i-1]):
                sum += down
                down += 1
                i += 1
            if down > peak:
                sum += (down-peak)
        return sum
