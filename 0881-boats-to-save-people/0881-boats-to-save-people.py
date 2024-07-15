class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i = 0
        j = len(people) - 1
        res = 0
        while i <= j:
            curLimit = limit
            if people[j] <= curLimit:
                curLimit -= people[j]
                j -= 1
            if people[i] <= curLimit:
                curLimit -= people[i]
                i += 1
            res += 1
        return res
