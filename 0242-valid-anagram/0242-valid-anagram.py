class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = 0
            counts[ch] +=1
        # print(counts)
        for ch in t:
            if ch not in counts:
                return False
            if counts[ch] == 1:
                del counts[ch]
            else: 
                counts[ch] -=1
        return True if len(counts) == 0 else False