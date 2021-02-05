class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        if not A or not A[0]:
            return []
        res = []
        m, n = len(A), len(A[0])
        a, b, c, d = 0, m - 1, 0, n - 1
        while len(res) < m * n:
            for i in range(c, d + 1):
                res.append(A[a][i])
            a += 1
            for i in range(a, b + 1):
                res.append(A[i][d])
            d -= 1
            for i in range(d, c - 1, -1):
                res.append(A[b][i])
            b -= 1
            for i in range(b, a - 1, -1):
                res.append(A[i][c])
            c += 1
        return res[:m * n]
'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y = 0, 0
        d = 0
        for i in range(1, n * n + 1):
            res[x][y] = i
            x += dirs[d][0]
            y += dirs[d][1]
            if not (0 <= x < n and 0 <= y < n and res[x][y] == 0):
                x -= dirs[d][0]
                y -= dirs[d][1]
                d = (d + 1) % 4
                x += dirs[d][0]
                y += dirs[d][1]
        return res