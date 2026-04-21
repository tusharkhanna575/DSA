class Solution:
    def combinationSum3(self, k, n):
        # your code goes here
        """
        T.C. : O(2^9 * k)
        S.C. : O(k)
        """

        def help(sum, last, nums, k, ans):
            if sum == 0 and len(nums) == k:
                ans.append(nums[:])
                return
            if sum <= 0 or len(nums) > k:
                return
            for i in range(last, 10):
                if i <= sum:
                    nums.append(i)
                    help(sum-i, i+1, nums, k, ans)
                    nums.pop()
                else:
                    break

        ans = []
        nums = []
        help(n, 1, nums, k, ans)
        return ans
