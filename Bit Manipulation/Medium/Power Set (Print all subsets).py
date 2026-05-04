class Solution:
    def powerSet(self, nums):
        """
        T.C. : O(n * 2^n) where n is the length of the input array as we are generating 2^n subsets and each subset can take O(n) time to generate
        S.C. : O(n * 2^n) for storing all the subsets in the answer list
        """
        # your code goes here
        n = len(nums)
        ans = []
        cnt = 1 << n
        for i in range(cnt):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(nums[j])
            ans.append(subset)
        return ans
