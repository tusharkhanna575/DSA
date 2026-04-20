class Solution:
    def combinationSum(self, candidates, k):
        """
        T.C. : O(k * n^(k/min(candidates))
        S.C. : O(k/min(candidates))
        """
        # your code goes here

        def help(v, idx, sum, v2, ans):
            if sum == 0:
                ans.append(v2[:])
                return
            if sum < 0 or idx < 0:
                return
            help(v, idx-1, sum, v2, ans)
            v2.append(v[idx])
            help(v, idx, sum-v[idx], v2, ans)
            v2.pop()

        ans = []
        help(candidates, len(candidates)-1, k, [], ans)
        return ans
