class Solution:

    """
    T.C. : O(n)
    S.C. : O(1)
    """

    def arraySortedOrNot(self, arr, n):
        for i in range(1, n):
            if not (arr[i - 1] <= arr[i]):
                return False
        return True
