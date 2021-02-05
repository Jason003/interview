class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if (m == 0 or nums[m - 1] != nums[m]) and (m == n - 1 or nums[m + 1] != nums[m]): return nums[m]
            if m % 2 == 0:
                if m > 0 and nums[m] == nums[m - 1]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if m > 0 and nums[m] == nums[m - 1]:
                    l = m + 1
                else:
                    r = m - 1
