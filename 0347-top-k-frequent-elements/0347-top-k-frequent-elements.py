class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for key, val in count.items():
            res.append((val, key))
        res.sort()

        result = []
        while k:
            result.append(res.pop()[1])
            k -= 1
        return result
