class ArrayQueue:

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.pop(0)

    def peek(self):
        return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0
