class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        baskets = {}

        def putToDict(key, val):
            if key not in baskets:
                baskets[key] = 0
            baskets[key] += val

        def delFrom(key, val):
            if baskets[key] == 1:
                del baskets[key]
            else:
                baskets[key] -= val

        i = 0
        res = 0
        for j in range(len(fruits)):
            fruit_type = fruits[j]
            putToDict(fruit_type, 1)
            while len(baskets) > 2:
                delFrom(fruits[i], 1)
                i += 1
            res = max(j - i + 1, res)
        return res
