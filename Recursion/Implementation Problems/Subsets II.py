from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        T.C. : O(n * 2^n)
        S.C. : O(n * 2^n)
        """

        def help(idx, n, curr, ans):
            if idx == n:
                ans.add(tuple(curr))
                return
            help(idx+1, n, curr, ans)
            curr.append(nums[idx])
            help(idx+1, n, curr, ans)
            curr.pop()

        nums.sort()
        n = len(nums)
        ans = set()
        curr = []
        help(0, n, curr, ans)
        return [list(x) for x in ans]
