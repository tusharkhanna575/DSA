class Solution:
    def reversePairs(self, nums):
        """
        T.C. : O(nlogn)
        S.C. : O(n)
        """

        def mergeSort(arr, low, high):
            res = 0
            if low >= high:
                return res
            mid = (low+high)//2
            res += mergeSort(arr, low, mid)
            res += mergeSort(arr, mid+1, high)
            res += countPairs(arr, low, mid, high)
            merge(arr, low, mid, high)
            return res

        def countPairs(arr, low, mid, high):
            right = mid+1
            res = 0
            for i in range(low, mid+1):
                while (right <= high and arr[i] > 2*arr[right]):
                    right += 1
                res += (right-(mid+1))
            return res

        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid+1
            while (left <= mid and right <= high):
                if (arr[left] <= arr[right]):
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while (left <= mid):
                temp.append(arr[left])
                left += 1
            while (right <= high):
                temp.append(arr[right])
                right += 1
            for i in range(low, high+1):
                arr[i] = temp[i-low]

        return mergeSort(nums, 0, len(nums)-1)
