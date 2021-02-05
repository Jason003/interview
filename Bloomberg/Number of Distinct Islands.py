class Solution:
    def numDistinctIslands(self, A) -> int:
        seen = set()
        m, n = len(A), len(A[0])
        def dfs(i, j, curr):
            if 0 <= i < m and 0 <= j < n and A[i][j]:
                A[i][j] = 0
                curr.append((i, j))
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    dfs(i + di, j + dj, curr)
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    curr = []
                    dfs(i, j, curr)
                    ref = sorted(curr)[0]
                    seen.add(tuple([(i - ref[0], j - ref[1]) for i, j in curr]))
        return len(seen)