class Solution:

    def longestSubarrayWithSum(self, arr, k):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) as we are not using any extra space
        """
        n = len(arr)
        maxLength = 0
        sum, left = 0, 0

        for right in range(n):
            sum += arr[right]

            while (sum > k):
                sum -= arr[left]
                left += 1

            maxLength = max(maxLength, right-left+1)

        return maxLength
