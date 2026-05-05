class Solution:
    def maxMeetings(self, start, end):
        # your code goes here
        """
        T.C. : O(nlogn) for sorting the meetings array + O(n) for iterating through the meetings array
        S.C. : O(n) for the meetings array to store the start time, end time, and index of each meeting
        """
        n = len(start)
        meeting = []
        for i in range(n):
            meeting.append((start[i], end[i], i))

        meeting.sort(key=lambda x: x[1])
        limit = meeting[0][1]
        ans = 1

        for i in range(n):
            if meeting[i][0] > limit:
                limit = meeting[i][1]
                ans += 1
        return ans
