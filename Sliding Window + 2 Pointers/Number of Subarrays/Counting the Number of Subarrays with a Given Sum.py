class Solution:

    def helper(self, arr, k):
        if (k < 0):
            return 0
        n = len(arr)
        cnt = 0
        i = 0
        for j in range(n):
            k -= arr[j]
            while (k < 0):
                k += arr[i]
                i += 1
            cnt += (j-i+1)
        return cnt

    def numSubarraysWithSum(self, arr, k):
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) as we are not using any extra space
        """
        return self.helper(arr, k) - self.helper(arr, k-1)
