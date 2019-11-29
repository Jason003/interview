# 需要输出所有可能呢？
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(idx):
            if idx in d: return d[idx]
            if idx >= len(s): return 1
            if s[idx] == '0': return 0
            if idx < len(s) - 1 and (s[idx] == '1' or s[idx] == '2' and '0' <= s[idx + 1] <= '6'):
                d[idx] = dfs(idx + 1) + dfs(idx + 2)
            else:
                d[idx] = dfs(idx + 1)
            return d[idx]
        d = {}
        return dfs(0)