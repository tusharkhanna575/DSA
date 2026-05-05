class Solution(object):
    def isValid(self, s):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input string as we are iterating through all the characters of the string
        S.C. : O(1) as we are using only two variables to store the minimum and maximum number of open parentheses that can be formed at any point in the string
        """
        min, max = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                min += 1
                max += 1
            elif s[i] == ")":
                min -= 1
                max -= 1
            elif s[i] == "*":
                min -= 1
                max += 1
            if max < 0:
                return False
            if min < 0:
                min = 0
        return (min == 0)
