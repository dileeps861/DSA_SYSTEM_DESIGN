class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def findValue(self, timestamps, timestamp):
        if len(timestamps) == 0:
            return ""
        low = 0
        high = len(timestamps) - 1
        while low < high:
            mid = low + (high - low) // 2
            # print(low, mid, high)
            midTS, midVal = timestamps[mid]
            if midTS == timestamp:
                return midVal
            if midTS < timestamp:
                low = mid + 1
            else:
                high = mid
        return timestamps[low][1]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        timestamps = self.cache[key]
        return self.findValue(timestamps, timestamp)



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)