class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j, cur = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or cur > 0:
            cur += int(a[i] if i >= 0 else '0') + int(b[j] if j >= 0 else '0')
            res.append(str(cur % 2))
            cur //= 2
            i, j = i - 1, j - 1
        return ''.join(res)[::-1]