class Solution:
    def findPlatform(self, Arrival, Departure):
        # your code goes here
        """
        T.C. : O(nlogn) for sorting the arrival and departure arrays + O(n) for iterating through the arrival and departure arrays
        S.C. : O(1) for the four variables to store the count of platforms required, the current count of platforms, and the indices for iterating through the arrival and departure arrays
        """
        Arrival.sort()
        Departure.sort()

        i, j = 0, 0
        ans, curr = 0, 0
        n = len(Arrival)

        while (i < n):
            if (Arrival[i] <= Departure[j]):
                curr += 1
                i += 1
            else:
                j += 1
                curr -= 1
            ans = max(ans, curr)
        return ans
