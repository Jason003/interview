class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        h = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            # monotonus increasing stack storing corresponding indexes
            stack = []
            for j in range(n + 1):
                while stack and h[stack[-1]] > h[j]:
                    res = max(res, h[stack.pop()] * (j if not stack else j - stack[-1] - 1)) # closest left index which is lower than h[stack.pop()] is stack[-1] after popping and right index which is lower than h[stack.pop()] is j
                stack.append(j)
        return res