class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def _fillStack2(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))

    def pop(self) -> int:
        self._fillStack2()
        return self.stack2.pop(-1)

    def peek(self) -> int:
        self._fillStack2()
        return self.stack2[-1]

    def empty(self) -> bool:
        self._fillStack2()
        return len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
