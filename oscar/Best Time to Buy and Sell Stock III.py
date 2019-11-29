class Solution1:
    def maxProfit(self, prices) -> int:
        mn, res = float('inf'), 0
        for p in prices:
            mn = min(mn, p)
            res = max(res, p - mn)
        return res

class Solution2:
    def maxProfit(self, prices) -> int:
        return sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)] or [0])

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
'''
class Solution3:
    def maxProfit(self, prices) -> int:
        def helper(K):
            ik0, ik1 = [0] * (K + 1), [-float('inf')] * (K + 1)
            for p in prices:
                for k in range(1, K + 1):
                    ik0[k] = max(ik0[k], ik1[k] + p)
                    ik1[k] = max(ik1[k], ik0[k - 1] - p)
            return ik0[K]
        return helper(2)