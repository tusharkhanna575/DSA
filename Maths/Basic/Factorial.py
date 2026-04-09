class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

# OR
# class Solution:
#     def factorial(self, n):
#         if n == 0 or n == 1:
#             return 1
#         return n * self.factorial(n - 1)


# OR
# import math
# class Solution:
#     def factorial(self, n):
#         return math.factorial(n)