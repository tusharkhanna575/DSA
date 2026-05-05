class Solution:
    def solve(self, bt):
        # your code goes here
        """
        T.C. : O(nlogn) for sorting the burst time array + O(n) for iterating through the burst time array
        S.C. : O(1) for the two variables to store the total waiting time and the total burst time
        """
        bt.sort()
        wait, total = 0, 0
        for i in bt:
            wait += total
            total += i
        return wait//len(bt)
