from collections import Counter

class Solution:
    def singleNumber(self, nums):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1)
        """
        xor = 0
        for i in nums:
            xor ^= i
        return xor

    def singleNumber(self, nums):
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(n) for hashmap to store the count of each element in the array
        """
        map = Counter(nums)
        for i, j in map.items():
            if j == 1:
                return i
        return -1
