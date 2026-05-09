class Solution:
    def numSubarraysWithSum(self, nums, goal):
        # your code goes here
        """
        T.C. : O(4*n)
        S.C. : O(1)"""

        def help(arr, goal):
            if goal < 0:
                return 0
            l, r = 0, 0
            sum_val, cnt = 0, 0
            while r < len(nums):
                sum_val += nums[r]
                while sum_val > goal:
                    sum_val -= nums[l]
                    l += 1
                cnt += (r-l+1)
                r += 1
            return cnt

        return help(nums, goal) - help(nums, goal-1)
