# -*- coding: utf-8 -*-
# @Time : 2020/12/10 21:04
# @Author : Jiefan
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]: return 0
        dirs, m, n = [[0, 1], [1, 0], [-1, 0], [0, -1]], len(matrix), len(matrix[0])
        mem = [[0] * n for _ in range(m)]
        def dfs(i, j, pre):
            if i >= m or i < 0 or j >= n or j < 0 or matrix[i][j] <= pre: return []
            if mem[i][j]: return mem[i][j]
            res = []
            for d in dirs:
                ii, jj = i + d[0], j + d[1]
                res = max(res, [matrix[i][j]] + dfs(ii, jj, matrix[i][j]), key = len)
            mem[i][j] = res
            return res
        return len(max([dfs(i, j, -float("inf")) for i in range(m) for j in range(n)], key = len))