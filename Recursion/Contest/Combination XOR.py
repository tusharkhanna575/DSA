class Solution:
    def combinationXor(self, nums, k):
        """
        T.C. : O(2^n)
        S.C. : O(n)
        """

        def help(idx, xor, curr, nums, k, res):
            if idx == len(nums):
                if xor == k and curr:
                    res.append(curr[:])
                return

            curr.append(nums[idx])
            help(idx+1, xor ^ nums[idx], curr, nums, k, res)

            curr.pop()
            help(idx+1, xor, curr, nums, k, res)

        res = []
        temp = []
        help(0, 0, temp, nums, k, res)
        return res
