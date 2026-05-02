def removeLastSetBit(n):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    return n & (n - 1)
