class Solution:

    """
    T.C. : O(n)
    S.C. : O(1)
    """

    def reverse(self, arr: list, n: int) -> None:
        low, high = 0, n - 1
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
