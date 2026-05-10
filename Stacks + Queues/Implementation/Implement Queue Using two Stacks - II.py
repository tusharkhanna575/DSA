class StackQueue:

    """
    T.C. : O(1) for push, O(n) for pop and peek
    S.C. : O(2 * n)
    """

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        self.st1.append(x)

    def pop(self):
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        if not self.st2:
            return -1
        return self.st2.pop()

    def peek(self):
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        if not self.st2:
            return -1
        return self.st2[-1]

    def isEmpty(self):
        return not self.st1 and not self.st2
