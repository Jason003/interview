# The array may contain duplicates.
class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if nums[mi] > nums[hi]: # left part is sorted:
                lo = mi + 1
            elif nums[mi] < nums[hi]: # right part is sorted
                hi = mi
            else: hi -= 1
        return nums[lo]