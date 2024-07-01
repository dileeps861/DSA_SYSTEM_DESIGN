class Solution:
    def longestPalindrome(self, s: str) -> str:

        # approach: for each substring if ith and jth chars are same and the i+1 and j -1 substring is a palindrome the substring i to j is also palindrome
        # how do we get this? we start from subtring of len 1 then len 2 then 3 and so far until n
        # if we look the decision tree the string will be reparested many tines

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # fill the array of length 1
        for i in range(n):
            dp[i][i] = True

        res = [0, 0]
        # fill the array of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res = [i, i + 1]

        for x in range(3, n + 1):
            for j in range(x - 1, n):
                i = j - x + 1
                k = i + 1
                l = j - 1
                # When the x is of size 2 which means j-1 and i+1 will be equals
                if dp[k][l] and s[i] == s[j]:
                    dp[i][j] = True
                    res = [i, j]
        return s[res[0] : res[1] + 1]
