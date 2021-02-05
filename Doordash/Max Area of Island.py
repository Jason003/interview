
'''
if the map is too big:
1.我用的dfs 数据大了会stack overflow 然后说可以用bfs解决这个问题
2.数据有可能大到内存存不下整个地图。我就开始瞎说说可以每次读一行，然后再用一个map存每一列的信息。key是col index，value存这个col对应的数字，之前遍历过的总面积大小，以及之前行相连同一数字的index用来dedupe。具体细节我也没有想清楚。。。
'''
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        dirs, m, n, res = [[0,1],[0,-1],[1,0],[-1,0]], len(grid), len(grid[0]), 0
        def dfs(x, y, c):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] in (0, ''): return 0
            grid[x][y], res = '', 1
            for d in dirs:
                res += dfs(x + d[0], y + d[1], c)
            return res
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, grid[i][j]))
        return res

import collections
# get areas of islands
def areasOfIslands(grid):
    areas = []
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        nonlocal area
        if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
            return
        area += 1
        grid[i][j] = 0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(i + di, j + dj)
    for i in range(m):
        for j in range(n):
            area = 0
            dfs(i, j)
            if area:
                areas.append(area)
    return areas

print(areasOfIslands([[1,1,1,1],[1,0,0,0],[0,0,0,0],[1,0,0,0],[1,1,0,0]]))