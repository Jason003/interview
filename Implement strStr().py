class Solution:
    def strStr(self, s: str, p: str) -> int:
        if len(s) < len(p): return -1

        def getInt(c):
            return ord(c) - ord('a')

        def getHash(s):
            res = 0
            for c in s:
                res = res * 26 + getInt(c)
            return res

        h = getHash(p)
        curr = getHash(s[:len(p)])
        for i in range(len(p), len(s)):
            if curr == h:
                return i - len(p)
            curr = (curr - getInt(s[i - len(p)]) * (26 ** (len(p) - 1))) * 26 + getInt(s[i])
        return len(s) - len(p) if curr == h else -1

        # if not p: return 0
        # if len(s) < len(p): return -1
        # for i in range(len(s) - len(p) + 1):
        #     if s[i : i + len(p)] == p: return i
        # return -1

        # m, n = len(s), len(p)
        # lps = [0] * n
        # l, i = 0, 1
        # while i < n:
        #     if p[i] == p[l]:
        #         l += 1
        #         lps[i] = l
        #         i += 1
        #     else:
        #         if l > 0: l = lps[l - 1]
        #         else: i += 1
        # i, j = 0, 0
        # while i < m:
        #     if s[i] == p[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         if j > 0: j = lps[j - 1]
        #         else: i += 1
        #     if j == n: return i - j
        # return -1