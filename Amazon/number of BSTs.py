class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        def helper(lo, hi):
            if hi <= lo: return 1
            if (lo, hi) in d: return d[(lo, hi)]
            res = 0
            for i in range(lo, hi + 1):
                res += helper(lo, i - 1) * helper(i + 1, hi)
            d[(lo, hi)] = res
            return res
        return helper(1, n)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1): # number of nodes
            for j in range(1, i + 1): # root number
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]