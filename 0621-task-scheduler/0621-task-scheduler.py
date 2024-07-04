class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        res = 0
        while mp:
            count = 0
            # Try to execute up to n+1 tasks (if available)
            for key, value in mp.most_common(n + 1):
                res += 1
                if value == 1:
                    del mp[key]
                else:
                    mp[key] = value - 1
                count += 1

            # If there are still tasks left, add idle periods
            if mp:
                res += max(0, n - count + 1)

        return res
