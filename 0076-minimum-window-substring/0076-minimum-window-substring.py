class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tC = Counter(t)
        
        i = 0
        fres = []
        mx = float("inf")
        sC = defaultdict(int)
        def check():
            for key, val in tC.items():
                if sC[key] < val:
                    return False
            return True

        for j in range(len(s)):
            if s[j] not in tC:
                continue
            
            sC[s[j]] += 1
            
            while i < j and (s[i] not in tC or sC[s[i]] > tC[s[i]]):
                if s[i] in sC and sC[s[i]] > 0:
                    sC[s[i]] -= 1
                i += 1

            if check() and mx > (j-i+1):
                mx = (j-i+1)
                fres = [i,j]
        if len(fres) == 0:
            return ""
        return s[fres[0]: fres[1]+1]
