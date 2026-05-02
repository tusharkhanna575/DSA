def checkForPowerOf2(n):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
