class Solution:
    def maxProfit(self, k: int, prices) -> int:
        n = len(prices)
        if k > n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        ik0, ik1 = [0] * (k + 1), [-prices[0]] * (k + 1)
        # ik0[i] means the max profit which we can get for current price and i transactions while we don't have stocks on hand
        # ik1[i] means the max profit which we can get for current price and i transactions while we have stocks on hand
        for p in prices:
            for i in range(1, k + 1):
                ik0[i] = max(ik0[i], ik1[i] + p)
                ik1[i] = max(ik1[i], ik0[i - 1] - p)
        return ik0[-1]