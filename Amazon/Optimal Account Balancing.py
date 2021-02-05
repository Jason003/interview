import functools, collections
class Solution:
    def minTransfers(self, transactions) -> int:
        balance = collections.Counter()
        for i, j, v in transactions:
            balance[i] -= v
            balance[j] += v
        value = [v for v in balance.values() if v != 0]
        n = len(value)
        self.res = float('inf')

        def dfs(idx, curr):
            if curr >= self.res: return
            while idx < n and value[idx] == 0:
                idx += 1
            if idx == n:
                self.res = min(self.res, curr)
                return
            for i in range(idx + 1, n):
                if value[i] * value[idx] < 0:
                    value[i] += value[idx]
                    dfs(idx + 1, curr + 1)
                    value[i] -= value[idx]

        dfs(0, 0)
        return self.res