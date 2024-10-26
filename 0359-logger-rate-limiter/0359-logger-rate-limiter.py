class Logger:

    def __init__(self):
        self.messageCache = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messageCache and self.messageCache[message] > timestamp - 10:
            return False
        self.messageCache[message] = timestamp

        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)