class Solution:
    def distinctExpressions(self, nums):
        """
        T.C. : O(2^n)
        S.C. : O(2^n)
        """

        def help(idx, curr):
            if idx == len(nums):
                ans.add(curr)
                return

            help(idx+1, curr+nums[idx])
            help(idx+1, curr-nums[idx])

        ans = set()
        help(1, nums[0])
        return sorted(list(ans))
