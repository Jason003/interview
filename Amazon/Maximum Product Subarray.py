class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, mx, mn = -float('inf'), 1, 1
        for n in nums:
            if n < 0: mx, mn = mn, mx
            mx = max(mx * n, n)
            mn = min(mn * n, n)
            res = max(res, mx)
        return res