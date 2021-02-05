class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0: continue
        #         grid[i][j] += min(grid[i - 1][j] if i > 0 else float('inf'), grid[i][j - 1] if j > 0 else float('inf'))
        # return grid[-1][-1]
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                dp[j] = grid[i][j] + min(dp[j] if i > 0 else float('inf'), dp[j - 1] if j > 0 else float('inf'))
        return dp[-1]