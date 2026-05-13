class Solution:
    def trap(self, height):
        """
        T.C. : O(n)
        S.C. : O(1)
        """
        n = len(height)
        leftMax = rightMax = total = 0
        l, r = 0, n-1

        while l < r:
            if height[l] <= height[r]:
                if leftMax > height[l]:
                    total += (leftMax-height[l])
                else:
                    leftMax = height[l]
                l += 1
            else:
                if rightMax > height[r]:
                    total += (rightMax-height[r])
                else:
                    rightMax = height[r]
                r -= 1
        return total
