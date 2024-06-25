class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            j = i
            while j:
                count +=1
                j &= j-1
            res.append(count)
        return res
