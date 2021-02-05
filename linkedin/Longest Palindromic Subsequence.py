class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2: return n
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)
                else:
                    dp[i][j] = max(dp[i + 1][j] if i + 1 < n else -float('inf'),
                                   dp[i][j - 1] if j - 1 >= 0 else -float('inf'))
        return dp[0][n - 1]

        # dp = [0] * n
        # for i in range(n - 1, -1, -1):
        #     dp[i], tep = 1, dp[i]
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             tep, dp[j] = dp[j], tep + 2
        #         else:
        #             tep, dp[j] = dp[j], max(dp[j - 1], dp[j])
        # return dp[-1]