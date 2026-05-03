from collections import Counter


class Solution:
    def singleNumber(self, nums):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(n) for hashmap to store the count of each element in the array
        """
        map = Counter(nums)
        for i, j in map.items():
            if j == 1:
                return i
        return -1

    def singleNumber(self, nums):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) for the two variables to store the single numbers
        """
        one = two = 0
        for i in range(len(nums)):
            one = (one ^ nums[i]) & ~two
            two = (two ^ nums[i]) & ~one
        return one
