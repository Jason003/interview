class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = [] # result
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

'''
3 sum closest
'''
class Solution:
    def threeSumClosest(self, nums, target):
        nums, diff, n, res = sorted(nums), float("inf"), len(nums), 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                if s > target: r -= 1
                elif s < target: l += 1
                else: return target
        return res

'''
3Sum Smaller


Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
'''
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums, n, res = sorted(nums), len(nums), 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res