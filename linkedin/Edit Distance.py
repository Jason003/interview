class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[j] = dp[j - 1] + 1
                elif j == 0:
                    dp[j] = dp[j] + 1
                elif word1[i - 1] == word2[j - 1]:
                    dp[j] = pre[j - 1]
                else:
                    dp[j] = min(pre[j - 1], dp[j], dp[j - 1]) + 1
            pre = dp[:]
        return dp[-1]

        # m, n = len(word1), len(word2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)] # dp[i][j] means the distance between word1[:i] and word2[:j]
        # for i in range(m + 1):
        #     for j in range(n + 1):
        #         if i == 0 and j == 0: continue
        #         elif i == 0: dp[i][j] = dp[i][j - 1] + 1
        #         elif j == 0: dp[i][j] = dp[i - 1][j] + 1
        #         elif word1[i - 1] == word2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
        #         else: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        # return dp[-1][-1]