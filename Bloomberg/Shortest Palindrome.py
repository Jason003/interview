class Solution:
    def shortestPalindrome(self, s: str) -> str: # O(n ^ 2)
        if not s: return ''
        def isPal(s, l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        for r in range(len(s) - 1, -1, -1):
            if isPal(s, 0, r):
                return s[r+1:][::-1] + s

### kmp
class Solution:
    def shortestPalindrome(self, s: str) -> str: # O(n)
        n = len(s)
        i, j = 0, 2 * n
        if n == 0: return ''
        cs = [''] * (2 * n + 1)
        for c in s:
            cs[i] = c
            cs[j] = c
            i += 1
            j -= 1
        cs[n] = '#'

        # kmp
        kmp = [0] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            length = kmp[i - 1]
            while length and cs[length] != cs[i]:
                length = kmp[length - 1]
            if cs[i] == cs[length]:
                length += 1
            kmp[i] = length
        return ''.join(cs[n + 1: 2 * n - kmp[-2]]) + s

# 'aaba' -> 'aaba#abaa'