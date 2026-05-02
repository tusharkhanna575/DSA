def countTheNumOfSetBits(n):
    """
    T.C. : O(log n) where n is the input number as we are iterating through all the bits of the number
    S.C. : O(1)
    """
    cnt = 0
    while (n != 0):
        cnt += 1
        n = n & (n-1)
    return cnt


def countTheNumOfSetBits(n):
    """
    T.C. : O(log n) where n is the input number as we are iterating through all the bits of the number
    S.C. : O(1)
    """
    cnt = 0
    while (n != 0):
        cnt += (n & 1)
        n = n >> 1
    return cnt
