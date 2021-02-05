class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dirs, mod, self.d = [[1, 0], [-1, 0], [0, 1], [0, -1]], 10 ** 9 + 7, {}

        def dfs(x, y, k):
            if (x, y, k) in self.d: return self.d[(x, y, k)]
            if x >= m or x < 0 or y >= n or y < 0: return 1
            if k <= 0: return 0
            res = 0
            for d in dirs:
                res = (res + dfs(x + d[0], y + d[1], k - 1)) % mod
            self.d[(x, y, k)] = res
            return res

        return dfs(i, j, N)
