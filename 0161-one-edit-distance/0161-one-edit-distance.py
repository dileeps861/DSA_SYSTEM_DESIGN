class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # First ensure that len(s) > len(t) if not swap both then do check recursively, so how we do is:
        # if the chars are same for s[i] == t[i] do i++ and j++ and isPassed = false
        # else three options:
        # 1. do i++ and j same and isPassed = True
        # 2. think of replacing with anyting else so i++, j++ and isPassed = True
        # base case whenever i > len(s) and j > len(t) then true or either above limits or isPassedTrue and
        m, n = len(s), len(t)
        if m > n:
            self.isOneEditDistance(t, s)
        if s == t:
            return False

        def dfs(i, j, isPassed):
            # Base cases
            if i >= m and j >= n:
                return True  # Bug #3: Should return isPassed instead of True
            
            if i >= m or j >= n:
                return not isPassed and abs(m - n) == 1  # Bug #4: Logic was incorrect
            
            if s[i] != t[j] and isPassed:
                return False
                
            # Bug #5: Logic for different operations was incorrect
            if s[i] == t[j]:
                return dfs(i + 1, j + 1, isPassed)
            else:
                # Try replace
                replace = dfs(i + 1, j + 1, True)
                # Try insert/delete
                return replace or dfs(i, j + 1, True) or dfs(i + 1, j, True)

        return dfs(0, 0, False)
