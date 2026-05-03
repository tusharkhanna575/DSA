class Solution:
    def minBitsFlip(self, start, goal):
        # your code goes here
        """
        T.C. : O(32) as we are iterating through 32 bits of the number
        S.C. : O(1)
        """
        ans = start ^ goal
        cnt = 0
        for i in range(32):
            if (ans & (1 << i)):
                cnt += 1
        return cnt

    def minBitsFlip(self, start, goal):
        # your code goes here
        """
        T.C. : O(log n) where n is the input number as we are iterating through all the bits of the number
        S.C. : O(1)
        """
        return bin(start ^ goal)[2:].count('1')
