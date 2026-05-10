class ListNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedListQueue:

    """
    T.C. : O(1) for push and pop
    S.C. : O(n)
    """

    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, x):
        element = ListNode(x)
        if self.start is None:
            self.start = element
            self.end = element
        else:
            self.end.next = element
            self.end = element
        self.size += 1

    def pop(self):
        if self.start is None:
            return -1
        val = self.start.data
        temp = self.start
        self.start = self.start.next
        del temp
        self.size -= 1
        if self.start is None:
            self.end = None
        return val

    def peek(self):
        if self.start is None:
            return -1
        return self.start.data

    def isEmpty(self):
        return self.size == 0
