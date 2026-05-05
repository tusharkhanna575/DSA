class Solution:
    def insertNewInterval(self, Intervals, newInterval):
        # your code goes here
        """
        T.C. : O(n) for iterating through the intervals array
        S.C. : O(n) for the result array to store the merged intervals"""
        res = []
        i = 0
        n = len(Intervals)

        while i < n and Intervals[i][1] < newInterval[0]:
            res.append(Intervals[i])
            i += 1

        while i < n and Intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], Intervals[i][0])
            newInterval[1] = max(newInterval[1], Intervals[i][1])
            i += 1

        res.append(newInterval)
        while (i < n):
            res.append(Intervals[i])
            i += 1

        return res
