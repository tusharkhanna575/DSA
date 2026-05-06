class Solution:
    def longestOnes(self, nums, k):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) as we are using only constant space to store the count of zeroes and the answer"""
        n = len(nums)
        l, r = 0, 0
        zero, ans = 0, 0
        while r < n:
            if nums[r] == 0:
                zero += 1
            if zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            if zero <= k:
                ans = max(ans, r-l+1)
            r += 1
        return ans
