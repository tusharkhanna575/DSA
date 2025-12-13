def optimized_bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

l = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", l)
sorted_l = bubble_sort(l)
print("Sorted array:", sorted_l)