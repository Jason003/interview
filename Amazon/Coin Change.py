# 注意问清楚是否全为正数！
'''
min coins to get the amount
'''
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = 0
            for j in range(1, amount + 1):
                dp[i][j] = min(dp[i - 1][j], (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else float('inf')) + 1)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

    def coinChange(self, coins, amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1


'''
Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
'''
class Solution:
    def change(self, amount: int, coins) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0)
        return dp[-1][-1]


class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]

# import collections
# follow up: what if there can be negative numbers
def change(amount: int, coins) -> int:
    res = 0
    coins.sort()
    def helper(idx, curr):
        nonlocal res
        if curr == amount:
            res += 1
        for i in range(idx, len(coins)):
            # if i > idx and coins[i] == coins[i - 1]: continue -> if we want to count distinctive sets
            helper(i + 1, curr + coins[i])
    helper(0, 0)
    return res
print(change(-2,[-1,-1,-1,0]))

