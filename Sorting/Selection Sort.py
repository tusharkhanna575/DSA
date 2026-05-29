class Solution:
    def selectionSort(self, nums):
        """
        T.C. : O(n^2)
        S.C. : O(1)
        """
        n = len(nums)
        for i in range(n - 1):
            mini = i
            for j in range(i + 1, n):
                if nums[j] < nums[mini]:
                    mini = j
            if mini != i:
                nums[i], nums[mini] = nums[mini], nums[i]
        return nums
