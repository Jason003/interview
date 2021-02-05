'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
'''


class Solution:
    def closedIsland(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m, n = len(A), len(A[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or A[i][j] != 0:
                return
            A[i][j] = 2
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + di, j + dj)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res