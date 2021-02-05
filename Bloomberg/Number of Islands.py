import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n

        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = 0

        # note this bfs must start from a point that is 1
        # it is rather equivalent to dfs
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = '0'
            while q:
                r, c = q.popleft()
                grid[r][c] = '0'
                for d in direct:
                    nr, nc = r + d[0], c + d[1]
                    if isValid(nr, nc) and grid[nr][nc] == '1':
                        q.append((nr, nc))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1

        return cnt