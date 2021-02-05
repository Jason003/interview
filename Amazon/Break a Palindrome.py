class Solution(object):
    def breakPalindrome(self, s):
        """
        :type palindrome: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return ''
        for i, c in enumerate(s[:n//2]):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i+1:]
        return s[:-1] + 'b'