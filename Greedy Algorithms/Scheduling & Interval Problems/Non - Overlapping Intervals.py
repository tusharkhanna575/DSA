class Solution:
    def MaximumNonOverlappingIntervals(self, Intervals):
        # your code goes here
        """
        T.C. : O(nlogn) for sorting the intervals + O(n) for iterating through the intervals
        S.C. : O(1) for the two variables to store the count of non-overlapping intervals and the end time of the last non-overlapping interval
        """
        n = len(Intervals)
        Intervals.sort(key=lambda x: x[1])
        ans = 1
        lastEndTime = Intervals[0][1]

        for i in range(n):
            if (Intervals[i][0] >= lastEndTime):
                ans += 1
                lastEndTime = Intervals[i][1]
        return n-ans
