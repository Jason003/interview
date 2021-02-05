'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n
        for i in range(1, n + 1):
            for k in range(1, int(n ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - k * k] + 1)
        return dp[-1]