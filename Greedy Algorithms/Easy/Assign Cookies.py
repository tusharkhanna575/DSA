class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        # your code goes here
        """
        T.C. : O(n log n + m log m) where n and m are the lengths of the Student and Cookie arrays respectively due to sorting
        S.C. : O(1) as we are using only constant extra space
        """
        n, m = len(Student), len(Cookie)
        l, r = 0, 0
        Student.sort()
        Cookie.sort()
        while (l < m and r < n):
            if Student[r] <= Cookie[l]:
                r += 1
            l += 1
        return r
