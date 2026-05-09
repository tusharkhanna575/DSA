class Solution:
    def numberOfOddSubarrays(self, nums, k):
        # your code goes here
        """
        T.C. : O(4*n)
        S.C. : O(1)
        """

        def help(arr, goal):
            if goal < 0:
                return 0
            l, r = 0, 0
            sum_val, cnt = 0, 0
            while r < len(arr):
                sum_val += (arr[r] % 2)
                while sum_val > goal:
                    sum_val -= (arr[l] % 2)
                    l += 1
                cnt += (r-l+1)
                r += 1
            return cnt

        return help(nums, k) - help(nums, k-1)
