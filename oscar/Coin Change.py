'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

'''

'''
可以先排序從大的開始嘗試
'''
class Solution:
    def change(self, amount: int, coins) -> int:
        # cache = {}
        # coins.sort()
        # def dfs(idx, cur):
        #     if cur == 0: return 1
        #     if cur < 0: return 0
        #     if (idx, cur) in cache: return cache[idx, cur]
        #     res = 0
        #     for i in range(idx, len(coins)):
        #         if cur >= coins[i]:
        #             res += dfs(i, cur - coins[i])
        #         else: break
        #     cache[idx, cur] = res
        #     return res
        # return dfs(0, amount)

        n = len(coins)
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]
