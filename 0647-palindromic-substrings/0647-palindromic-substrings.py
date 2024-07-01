class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # fill the array of length 1

        res = 0
        for i in range(n):
            dp[i][i] = True
            res += 1

        # fill the array of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1

        for x in range(3, n + 1):
            for j in range(x - 1, n):
                i = j - x + 1
                k = i + 1
                l = j - 1
                # When the x is of size 2 which means j-1 and i+1 will be equals
                if dp[k][l] and s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
        return res