class Solution:
    def subsetSums(self, nums):
        """
        T.C. : O(n * 2^n)
        S.C. : O(n * 2^n)
        """

        # your code goes here
        def help(idx, n, curr, ans):
            if idx == n:
                ans.append(sum(curr))
                return
            help(idx+1, n, curr, ans)
            curr.append(nums[idx])
            help(idx+1, n, curr, ans)
            curr.pop()

        n = len(nums)
        ans = []
        curr = []
        help(0, n, curr, ans)
        return ans
