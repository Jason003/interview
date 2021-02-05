'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0: continue
        #         dp[i][j] = (dp[i][j - 1] if j > 0 else 0) + (dp[i - 1][j] if i > 0 else 0)
        # return dp[-1][-1]

        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                dp[j] += (dp[j - 1] if j > 0 else 0)
        return dp[-1]

'''
follow up:
Now consider if some obstacles are added to the grids. How many unique paths would there be?

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 or obstacleGrid[i][j]: continue
                dp[i][j] = (dp[i][j - 1] if j > 0 else 0) + (dp[i - 1][j] if i > 0 else 0)
        return dp[-1][-1]


'''
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
'''
class Solution:
    def uniquePathsIII(self, grid: 'List[List[int]]') -> 'int':
        m, n, obs, self.res = len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: sx, sy = i, j
                elif grid[i][j] == 2: ex, ey = i, j
                elif grid[i][j] == -1: obs += 1
        def dfs(x, y, seen):
            if (x, y) == (ex, ey):
                if len(seen) == m * n - obs - 1: self.res += 1
                return
            if x >= m or y >= n or x < 0 or y < 0 or grid[x][y] == -1 or (x, y) in seen: return
            seen.add((x, y))
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(x + dx, y + dy, seen)
            seen.remove((x, y))
        dfs(sx, sy, set())
        return self.res