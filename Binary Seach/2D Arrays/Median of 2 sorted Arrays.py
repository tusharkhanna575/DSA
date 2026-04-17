class Solution:

    """
    T.C. : O(log(min(n1,n2)))
    S.C. : O(1)
    """

    def median(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        if n1 > n2:
            return self.median(arr2, arr1)
        low, high = 0, n1
        left = (n1+n2+1)//2
        n = n1+n2
        while (low <= high):
            mid1 = (low+high)//2
            mid2 = left-mid1
            l1, l2 = float('-inf'), float('-inf')
            r1, r2 = float('inf'), float('inf')
            if (mid1 < n1):
                r1 = arr1[mid1]
            if (mid2 < n2):
                r2 = arr2[mid2]
            if (mid1 >= 1):
                l1 = arr1[mid1-1]
            if (mid2 >= 1):
                l2 = arr2[mid2-1]
            if (l1 <= r2 and l2 <= r1):
                if (n % 2 == 1):
                    return max(l1, l2)
                return (max(l1, l2)+min(r1, r2))/2
            elif (l1 > r2):
                high = mid1-1
            else:
                low = mid1+1
        return 0
