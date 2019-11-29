class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        mapp = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        s = [mapp[c] for c in s]
        return sum([-s[i] if i < n - 1 and s[i + 1] > s[i] else s[i] for i in range(n)] or [0])
