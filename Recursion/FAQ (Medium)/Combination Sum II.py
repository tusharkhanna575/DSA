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

            if nums[idx] > sum:
                return

            arr.append(nums[idx])
            help(idx+1, sum-nums[idx], arr, nums)
            arr.pop()
            j = idx+1
            while j < len(nums) and nums[j] == nums[idx]:
                j += 1
            help(j, sum, arr, nums)

        candidates.sort()
        ans = []
        help(0, target, [], candidates)
        return ans
