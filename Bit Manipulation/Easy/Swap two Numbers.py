def swapTwoNumbers(a, b):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def swapTwoNumbers(a, b):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swapTwoNumbers(a, b):
    """
    T.C. : O(1)
    S.C. : O(1)
    """
    a, b = b, a
    return a, b
