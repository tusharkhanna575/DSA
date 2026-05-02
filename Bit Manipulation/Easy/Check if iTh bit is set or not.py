def checkForIthBit(n, i):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    return (1 & (n >> i)) != 0


def checkForIthBit(n, i):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    return (n & (1 << i)) != 0
