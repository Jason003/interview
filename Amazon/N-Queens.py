class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def judge(A):
            for i, a in enumerate(A[:-1]):
                if abs(a - A[-1]) == abs(len(A) - 1 - i):
                    return False
            return True
        res = []
        def dfs(idx, cur, candidates): # cur[i] means the position of queen in row i
            if idx == n:
                res.append(tuple(cur))
                return
            for i in candidates:
                if judge(cur + [i]):
                    dfs(idx + 1, cur + [i], candidates - {i})
        dfs(0, [], set(range(n)))
        def generate(A):
            n = len(A)
            res = [['.'] * n for i in range(n)]
            for i, n in enumerate(A):
                res[i][n] = 'Q'
            return [''.join(a) for a in res]
        return list(map(generate, res))