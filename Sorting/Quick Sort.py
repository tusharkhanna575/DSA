class Solution:

    def quickSort(self, nums):
        """
        T.C. : O(nlogn) on average, O(n^2) in worst case
        S.C. : O(logn) on average, O(n) in worst case
        """

        def quick_sort(arr, low, high):
            if low < high:
                pivot = partition(arr, low, high)
                quick_sort(arr, low, pivot-1)
                quick_sort(arr, pivot+1, high)

        def partition(arr, low, high):
            pivot = arr[low]
            i, j = low, high
            while i < j:
                while arr[i] <= pivot and i <= high-1:
                    i += 1
                while arr[j] > pivot and j >= low+1:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
            arr[low], arr[j] = arr[j], arr[low]
            return j

        quick_sort(nums, 0, len(nums)-1)
        return nums
