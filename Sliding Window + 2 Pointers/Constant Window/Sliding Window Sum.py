class Solution:

    def slidingWindowSum(self, nums, k):
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) as we are not using any extra space
        """
        n = len(nums)
        if (n < k):
            return []
        sum = 0
        for i in range(k):
            sum += nums[i]
        print(f"Sum of window 1: {sum}")

        for i in range(k, n):
            sum -= (nums[i-k] - nums[i])
            print(f"Sum of window {i-k+2}: {sum}")
