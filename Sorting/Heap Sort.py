import heapq

"""
T.C. : O(n logn)
S.C. : O(1)
"""


def min_heap_sort(nums):
    heapq.heapify(nums)
    sorted_nums = []
    while nums:
        sorted_nums.append(heapq.heappop(nums))
    return sorted_nums


l = [34, -6, 1, 0, 19, 2]
print(f"Unsorted Array: {l}")
min_sorted_l = min_heap_sort(l)
print(f"Sorted Array (min heap): {min_sorted_l}")
print(f"Sorted Array (max heap): {min_sorted_l[::-1]}")
