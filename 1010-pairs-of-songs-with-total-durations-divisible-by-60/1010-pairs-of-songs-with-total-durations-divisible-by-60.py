class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        cache = [0] * 60
        res = 0
        for num in time:
            rem = num % 60
            # Special case for remainder 0, the complement is also 0
            if rem == 0:
                comp = 0
            else:
                comp = 60 - rem

            res += cache[comp]
            cache[rem] += 1

        return res
