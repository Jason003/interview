class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        begin, end, pro, n, res = 0, 0, 1, len(nums), 0
        while end < n:
            pro *= nums[end]
            while pro >= k and begin < end:
                pro //= nums[begin]
                begin += 1
            if pro < k: res += end - begin + 1
            end += 1
        return res