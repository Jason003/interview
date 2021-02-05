class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            res ^= i
            res ^= num
        return res ^ len(nums)