class Solution:

    def mergeSort(self, nums):
        """
        T.C. : O(nlogn)
        S.C. : O(n)
        """

        def merge(arr, low, mid, high):
            temp = []
            left, right = low, mid + 1

            while left <= mid and right <= high:

                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1

                else:
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1

            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def mSort(nums, low, high):
            if low >= high:
                return

            mid = low + (high - low) // 2
            mSort(nums, low, mid)
            mSort(nums, mid + 1, high)
            merge(nums, low, mid, high)

        n = len(nums)
        mSort(nums, 0, n - 1)
        return nums
