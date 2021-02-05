'''
DFS vs BFS

The major difference between BFS and DFS is that BFS proceeds level by level while DFS follows first a path form the starting to the ending node (vertex), then another path from the start to end, and so on until all nodes are visited. Furthermore, BFS uses the queue for storing the nodes whereas DFS uses the stack for traversal of the nodes.

BFS is vertex-based algorithm while DFS is an edge-based algorithm.
Queue data structure is used in BFS. On the other hand, DFS uses stack or recursion.
Memory space is efficiently utilized in DFS while space utilization in BFS is not effective.
BFS is optimal algorithm (if the path cost is a non-decreasing function of d(depth). Normally, BFS is applied when all the actions have the same cost) while DFS is not optimal
DFS constructs narrow and long trees. As against, BFS constructs wide and short tree.

'''
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

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        dirs, m, n, res = [[1,0],[-1,0],[0,1],[0,-1]], len(grid), len(grid[0]), 0
        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0: return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for d in dirs:
                    dfs(i + d[0], j + d[1])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res

class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        grid[x][y] = '0'
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            xx, yy = x + dx, y + dy
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                                stack.append((xx, yy))
        return res


# follow up: if 2 is a part of city, find number of cities on each island
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]: return 0
    dirs, m, n, res = [[1,0],[-1,0],[0,1],[0,-1]], len(grid), len(grid[0]), 0
    islands = []
    seen = set()
    def dfs(i, j, mark, limit):
        if i >= m or j >= n or i < 0 or j < 0 or (i, j) in seen or limit and (i, j) not in limit:
            return
        if grid[i][j] in mark:
            island.add((i, j))
            seen.add((i, j))
            for d in dirs:
                dfs(i + d[0], j + d[1], mark, None)

    for i in range(m):
        for j in range(n):
            if grid[i][j] and (i, j) not in seen:
                island = set()
                res += 1
                dfs(i, j, {1, 2}, None)
                islands.append(island)
    for island in islands:
        cnt = 0
        seen = set()
        for i, j in island:
            if grid[i][j] == 2 and (i, j) not in seen:
                cnt += 1
                dfs(i, j, {2}, island)
        print(cnt)



    return islands

print(numIslands([[0,0,0,1],[2,2,2,2],[1,1,0,0],[0,0,2,0]]))
