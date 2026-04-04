class Solution:
    def reverse(self, arr: list, n: int) -> None:
        low, high = 0, n - 1
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1