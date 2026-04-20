from functools import lru_cache


class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        """
        T.C. : O(n^2)
        S.C. : O(n^2)
        """
        # your code goes here

        @lru_cache(None)
        def help(idx, sum):
            if idx == len(nums):
                return 1 if sum == 0 else 0
            if k < 0:
                return 0
            return help(idx+1, sum-nums[idx]) + help(idx+1, sum)

        return help(0, k)
