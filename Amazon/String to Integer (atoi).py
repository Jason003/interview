class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        res = 0
        neg = s[0] == '-'
        for c in (s if s[0] not in ('+', '-') else s[1:]):
            if c.isdigit():
                res = res * 10 + ord(c) - ord('0')
            else:
                break
        return max(-2 ** 31, min(res * (-1 if neg else 1), 2 ** 31 - 1))
