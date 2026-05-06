class Solution:
    def maxScore(self, cardScore, k):
        # your code goes here
        """
        T.C. : O(k) where k is the number of cards to be taken from the beginning or the end of the array as we are iterating through k elements of the array
        S.C. : O(1) as we are using only a constant amount of space to store the sum of the elements taken from the beginning and the end of the array
        """
        lsum, rsum = 0, 0
        ans = 0
        n = len(cardScore)

        for i in range(k):
            lsum += cardScore[i]

        ans = lsum
        rightIdx = n-1

        for i in range(k-1, -1, -1):
            lsum -= cardScore[i]
            rsum += cardScore[rightIdx]
            rightIdx -= 1
            ans = max(ans, lsum+rsum)

        return ans
