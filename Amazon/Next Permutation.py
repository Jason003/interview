class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return 
        j = n - 1
        while j >= 0:
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1