class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = defaultdict(int)
        mxCount = 0
        mxLen = 0
        n = len(s)
        i = 0
        for j in range(n):
            count[s[j]] = count[s[j]] + 1
            mxCount = max(mxCount, count[s[j]])
            while (j - i + 1 - k) > mxCount:
                count[s[i]] -= 1
                i += 1
            mxLen = max(mxLen, (j - i + 1))
        return mxLen
