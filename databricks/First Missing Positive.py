class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                tep = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tep - 1] = tep
                i -= 1
            i += 1
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1