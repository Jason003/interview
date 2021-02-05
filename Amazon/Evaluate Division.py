import collections
class Solution:
    def calcEquation(self, equations, values, queries):
        d = collections.defaultdict(dict)
        for [a, b], v in zip(equations, values):
            d[a][b], d[b][a] = v, 1 / v
        def dfs(i, j, seen):
            if i not in d or j not in d: return -1
            if i == j: return 1
            if j in d[i]: return d[i][j]
            if i in d[j]: return 1 / d[j][i]
            res = -1
            for k in d[i]:
                if k not in seen:
                    tep = dfs(k, j, seen | {k})
                    if tep != -1:
                        res = tep * d[i][k]
                        break
            if res != -1:
                d[i][j] = res
                d[j][i] = 1 / res
            return res
        res = []
        for i, j in queries:
            res.append(dfs(i, j, set()))
        return res