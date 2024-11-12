class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("inf")

    def push(self, val: int) -> None:
        self.minVal = min(val, self.minVal)
        self.stack.append((val, self.minVal))

    def pop(self) -> None:

        if self.stack:
            val, minVal = self.stack[-1]
            self.stack.pop(-1)
            if minVal <= self.minVal:
                if self.stack:
                    self.minVal = self.stack[-1][1]
                else:
                    self.minVal = float("inf")

    def top(self) -> int:
        # print(self.stack, True if self.stack else False)
        if self.stack:
            return self.stack[-1][0]
        return 0

    def getMin(self) -> int:
        # print(self.stack, True if self.stack else False)
        if self.stack:
            return self.stack[-1][1]
        return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
