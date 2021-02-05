class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, l, r, k): # select k-th smallest
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(nums, p + 1, r, k)
            else:
                return quickSelect(nums, l, p - 1, k)
        return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)