class Solution:

    """
    T.C. : O(n*logn)
    S.C. : O(1)
    """

    def findPages(self, nums, m):

        def help(arr, max_pages):
            student = 1
            pages_per_student = 0
            n = len(arr)
            for i in range(n):
                if ((pages_per_student+arr[i]) <= max_pages):
                    pages_per_student += arr[i]
                else:
                    student += 1
                    pages_per_student = arr[i]
            return student

        if len(nums) < m:
            return -1
        low = max(nums)
        high = sum(nums)
        while (low <= high):
            mid = (low+high)//2
            no_of_students = help(nums, mid)
            if no_of_students > m:
                low = mid+1
            else:
                high = mid-1
        return low
