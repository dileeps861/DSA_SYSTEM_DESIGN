class RandomizedSet:

    def __init__(self):
        self.st = dict()
        self.rndNum = []

    def insert(self, val: int) -> bool:
        if val in self.st:
            return False
        self.rndNum.append(val)
        self.st[val] = len(self.rndNum) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.st:
            return False

        lastVal = self.rndNum[len(self.rndNum) - 1]
        rmNumIdx = self.st[val]
        self.rndNum[rmNumIdx] = lastVal
        self.st[lastVal] = rmNumIdx
        del self.st[val]
        self.rndNum.pop()
        return True

    def getRandom(self) -> int:
        return self.rndNum[random.randint(0, len(self.st) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
