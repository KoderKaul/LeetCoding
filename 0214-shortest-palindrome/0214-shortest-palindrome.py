class Solution:
    def shortestPalindrome(self, s: str) -> str:
        palindromeStr = s[::-1]
        
        if s == palindromeStr:
            return s

        for i in range(len(s)):
            if s[:len(s) - i] == palindromeStr[i:]:
                return palindromeStr[:i] + s

        return ""
        