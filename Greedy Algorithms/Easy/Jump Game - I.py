class Solution:
    def canJump(self, nums):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) for the two variables to store the length of the input array and the maximum index that can be reached
        """
        n = len(nums)
        maxIdx = 0
        for i in range(n):
            if i > maxIdx:
                return False
            maxIdx = max(maxIdx, i+nums[i])
        return True
