class Solution:
    def combinationSum2(self, candidates, target):
        # your code goes here
        """
        T.C. : O(n * 2^n)
        S.C. : O(n)
        """

        def help(idx, sum, arr, nums):
            if sum == 0:
                ans.append(arr[:])
                return
            if ((sum < 0) or (idx == len(nums))):
                return
            arr.append(nums[idx])
            help(idx+1, sum-nums[idx], arr, nums)
            arr.pop()
            for i in range(idx+1, len(nums)):
                if nums[i] != nums[idx]:
                    help(i, sum, arr, nums)
                    return

        candidates.sort()
        ans = []
        help(0, target, [], candidates)
        return ans
