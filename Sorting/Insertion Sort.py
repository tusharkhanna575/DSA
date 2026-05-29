class Solution:
    def insertionSort(self, nums):
        """
        T.C. : O(n^2)
        S.C. : O(1)
        """
        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > curr:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = curr

        return nums
