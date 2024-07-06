class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.lower = 0
        self.upper = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q[self.upper] = value
        self.upper = self._movePointer(self.upper)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        item = self.q[self.lower]
        self.q[self.lower] = -1
        self.lower = self._movePointer(self.lower)

        if self.lower == self.upper:
            self.lower, self.upper = 0, 0
        return True

    def _movePointer(self, pointer):
        pointer += 1
        if pointer == self.k:
            pointer = 0
        return pointer

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.lower]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.upper - 1] if self.upper != 0 else self.q[self.k - 1]

    def isEmpty(self) -> bool:
        if self.lower == self.upper and self.q[self.lower] == -1:
            return True
        return False

    def isFull(self) -> bool:
        return self.lower == self.upper and self.q[self.lower] != -1

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()