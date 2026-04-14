class Solution:

    """
    T.C. : O(n)
    S.C. : O(1)
    """

    def factorial(self, n):
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

# OR
# class Solution:
#
#     """
#     T.C. : O(n)
#     S.C. : O(n)
#     """
#
#     def factorial(self, n):
#         if n == 0 or n == 1:
#             return 1
#         return n * self.factorial(n - 1)


# OR
# import math
# class Solution:
#
#     """
#     T.C. : O(1)
#     S.C. : O(1)
#     """
#
#     def factorial(self, n):
#         return math.factorial(n)
