class ArrayStack:

    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        return self.st.pop()

    def top(self):
        return self.st[-1]

    def isEmpty(self):
        return len(self.st) == 0
