'''
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
'''


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # binary search + string hashing
        from functools import reduce
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1

        def judge(l):
            p = 26 ** l % mod
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:l], 0)
            seen = {cur}
            for i in range(l, len(S)):
                cur = (cur * 26 + A[i] - p * A[i - l]) % mod
                if cur in seen: return i - l + 1
                seen.add(cur)

        lo, hi = 0, len(S)
        res = 0
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = judge(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res: res + lo]

