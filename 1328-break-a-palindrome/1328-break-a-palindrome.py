class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        if n > 1:
            return palindrome[:n - 1] + 'b'
        return ""
