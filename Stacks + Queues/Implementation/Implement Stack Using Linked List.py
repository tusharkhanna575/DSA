class ListNode:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedListStack:

    """
    T.C. : O(1) for push and pop
    S.C. : O(n)
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        e = ListNode(x, self.head)
        self.head = e
        self.size += 1

    def pop(self):
        if self.head is None:
            return -1
        val = self.head.data
        temp = self.head
        self.head = self.head.next
        del temp
        self.size -= 1
        return val

    def top(self):
        if self.head:
            return self.head.data
        return -1

    def isEmpty(self):
        return self.size == 0
