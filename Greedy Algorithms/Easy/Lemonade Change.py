class Solution:
    def lemonadeChange(self, bills):
        # your code goes here
        """
        T.C. : O(n) where n is the length of the input array as we are iterating through all the elements of the array
        S.C. : O(1) for the three variables to store the count of five, ten and twenty dollar bills"""
        five, ten, twenty = 0, 0, 0

        for i in bills:
            if i == 5:
                five += 1

            elif i == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False

            elif i == 20:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False

        return True
