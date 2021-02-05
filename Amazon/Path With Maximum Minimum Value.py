'''
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-maximum-minimum-value
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class DSU(object):
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R = len(A)
        C = len(A[0])
        n = R * C
        d = DSU(n)
        s = set()
        points = []
        for i in range(R):
            for j in range(C):
                points.append((A[i][j], i, j))
        points.sort()
        ans = min(A[0][0], A[R - 1][C - 1])
        s.add((0, 0))
        s.add((R - 1, C - 1))
        while d.find(0) != d.find(n - 1):
            p, x, y = points.pop()
            ans = min(ans, p)
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if (i, j) in s:
                    d.union(x * C + y, i * C + j)
                s.add((x, y))
        return ans
