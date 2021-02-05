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