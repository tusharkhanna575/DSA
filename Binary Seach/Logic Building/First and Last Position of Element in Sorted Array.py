from bisect import bisect_left, bisect_right
from typing import List


class Solution:

    """
    T.C. : O(logn)
    S.C. : O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1
        return [l, r] if l <= r else [-1, -1]
