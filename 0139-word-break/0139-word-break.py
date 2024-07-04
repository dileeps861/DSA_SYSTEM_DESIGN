class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * n
        wordSet = set(wordDict)
        def findWordBreak(i):
            if i >= n:
                return True
            if dp[i] is not None:
                return dp[i]
            dp[i] = False
            
            for j in range(i, n):
                subS = s[i:j+1]
                if subS in wordSet:
                    res = findWordBreak(j+1)
                    if res:
                        dp[i] = True
                        break
            return dp[i]
        
        return findWordBreak(0)