from collections import Counter


class Solution:
    def singleNumber(self, nums):
        # your code goes here
        """
        T.C. : O(n log n) where n is the length of the input array as we are iterating through all the elements of the array and sorting the result
        S.C. : O(n) for hashmap to store the count of each element in the array and the result array to store the single numbers
        """
        map = Counter(nums)
        ans = []
        for i, j in map.items():
            if j == 1:
                ans.append(i)
        return sorted(ans)

    def singleNumber(self, nums):
        # your code goes here
        """
        T.C. : O(2*n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) for the three variables to store the xor of all elements, the rightmost set bit and the two single numbers
        """
        xor = 0
        n = len(nums)
        for i in range(n):
            xor ^= nums[i]

        right = (xor & (xor-1)) ^ xor
        b1, b2 = 0, 0
        for i in range(n):
            if nums[i] & right:
                b1 ^= nums[i]
            else:
                b2 ^= nums[i]

        return [min(b1, b2), max(b1, b2)]
