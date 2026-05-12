class MinStack:

    """
    T.C. : O(1) for all operations
    S.C. : O(n) for stack and O(1) for minimum element
    """

    def __init__(self):
        self.st = []
        self.mini = None

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.mini = val
            return
        if val > self.mini:
            self.st.append(val)
        else:
            self.st.append(2*val-self.mini)
            self.mini = val

    def pop(self) -> None:
        if not self.st:
            return
        val = self.st.pop()
        if val < self.mini:
            self.mini = (2*self.mini)-val

    def top(self) -> int:
        if not self.st:
            return -1
        val = self.st[-1]
        if self.mini < val:
            return val
        return self.mini

    def getMin(self) -> int:
        return self.mini
