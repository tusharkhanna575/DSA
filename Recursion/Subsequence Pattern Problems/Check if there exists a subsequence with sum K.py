class Solution:
    def checkSubsequenceSum(self, nums, k):
        """
        T.C. : O(2^n)
        S.C. : O(n)
        """

        # your code goes here
        def help(idx, n, arr, k):
            if k == 0:
                return True
            if k < 0:
                return False
            if idx == n:
                return bool(k == 0)
            return bool(help(idx+1, n, arr, k-arr[idx]) or help(idx+1, n, arr, k))

        n = len(nums)
        return help(0, n, nums, k)
