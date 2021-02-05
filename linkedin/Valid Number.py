class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s: return False
        i, n = 0, len(s)
        if s[0] in ('+', '-'): i += 1
        pt, num = 0, 0 # number of points, number of digits
        while i < n and (s[i].isdigit() or s[i] == '.'):
            if s[i].isdigit(): num += 1
            else: pt += 1
            i += 1
        if pt > 1 or num < 1: return False
        if i < n and s[i] == 'e':
            i += 1
            pt, num = 0, 0
            if i < n and s[i] in ('+', '-'): i += 1
            while i < n and s[i].isdigit():
                num += 1
                i += 1
            if num < 1: return False
        return i == n