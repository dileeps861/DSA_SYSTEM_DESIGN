class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        cache = {}
        res = 0
        for num in time:
            rem = num % 60
            # Special case for remainder 0, the complement is also 0
            if rem == 0:
                comp = 0
            else:
                comp = 60 - rem

            if comp in cache:
                res += cache[comp]

            if rem not in cache:
                cache[rem] = 0
            cache[rem] += 1

        return res
