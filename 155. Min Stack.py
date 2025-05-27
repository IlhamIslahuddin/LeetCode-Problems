class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        try:
            self.stack.pop(-1)
        except:
            return -1

    def top(self) -> int:
        try:
            return self.stack[-1]
        except:
            return -1

    def getMin(self) -> int:
        try:
            return min(self.stack)
        except:
            return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
