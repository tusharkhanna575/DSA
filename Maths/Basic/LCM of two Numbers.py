class Solution:
    def GCD(self, n1, n2):
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 %= n2
            else:
                n2 %= n1
        if n1 == 0:
            return n2
        return n1

    def LCM(self, n1, n2):
        return (n1 * n2) // self.GCD(n1, n2)