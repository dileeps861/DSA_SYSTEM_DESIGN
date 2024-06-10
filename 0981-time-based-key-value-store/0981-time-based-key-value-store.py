class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))
        
    def binarysearch(self, timestamps, low, high, timestamp) -> str:

        while low <= high:
            mid = low + (high - low) // 2
            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            if timestamps[mid][0] > timestamp:
                high = mid - 1
            else:
                low = mid + 1
       
        return timestamps[high][1] if timestamps[high][0] <= timestamp else ""


    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.timemap[key]
        if not timestamps:
            return ""
        return self.binarysearch(timestamps, 0, len(timestamps) - 1, timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)