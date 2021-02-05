class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        m2, m3, m5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[m2] * 2, dp[m3] * 3, dp[m5] * 5)
            if dp[i] == dp[m2] * 2: m2 += 1
            if dp[i] == dp[m3] * 3: m3 += 1
            if dp[i] == dp[m5] * 5: m5 += 1
        return dp[-1]

