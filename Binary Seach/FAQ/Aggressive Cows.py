class Solution:
    def aggressiveCows(self, nums, k):

        def can_we_place(arr, dist, cows):
            cnt = 1
            last_coord = arr[0]
            for i in range(1, len(arr)):
                if ((arr[i]-last_coord) >= dist):
                    cnt += 1
                    last_coord = arr[i]
                if (cnt >= cows):
                    return True
            return False

        nums.sort()
        low = 1
        high = nums[-1]-nums[0]
        while (low <= high):
            mid = (low+high)//2
            if can_we_place(nums, mid, k):
                low = mid+1
            else:
                high = mid-1
        return high
