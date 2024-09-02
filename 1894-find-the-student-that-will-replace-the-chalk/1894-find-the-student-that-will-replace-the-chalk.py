class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalChalkNeeded = sum(chalk)
        extraChalk = k % totalChalkNeeded

        i = 0
        while i < len(chalk):
            if extraChalk < chalk[i]:
                return i
            extraChalk -= chalk[i]
            i += 1
        return -1
