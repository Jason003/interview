'''
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.
'''


class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        if not A or not A[0]: return 0
        n, m = len(A), len(A[0])
        r = [[0] * (m + 1) for _ in range(n + 1)]
        c = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                r[i][j + 1] = r[i][j] + A[i][j]
                c[i + 1][j] = c[i][j] + A[i][j]
        for l in range(n - 1, -1, -1):
            for i in range(n - l):
                for j in range(m - l):
                    if r[i][j + l + 1] - r[i][j] == r[i + l][j + l + 1] - r[i + l][j] == c[i + l + 1][j] - c[i][j] == \
                            c[i + l + 1][j + l] - c[i][j + l] == l + 1: return (l + 1) * (l + 1)
        return 0
