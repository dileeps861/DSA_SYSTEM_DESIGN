class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [None for _ in range(n+1)]
        chars = {1:'A', 2:'B',
            3:'C', 4:'D',
            5:'E', 6:'F',
            7:'G', 8:'H',
            9:'I', 10:'J',
            11:'K', 12:'L',
            13:'M', 14:'N', 
            15:'O', 16:'P',
            17:'Q', 18:'R',
            19:'S', 20:'T',
            21:'U', 22:'V',
            23:'W', 24:'X',
            25:'Y', 26:'Z'}
        def findWays(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if dp[i] is not None:
                return dp[i]

            res = 0
            if int(s[i]) in chars:
                res += findWays(i+1) 
            if i+1 < n and int(s[i:i+2]) in chars:
                res += findWays(i+2)
            dp[i] = res
            return res
        return findWays(0)