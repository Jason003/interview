'''
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        def judge(x):
            cnt = 1
            summ = 0
            for i in range(n):
                summ += nums[i]
                if summ > x:
                    cnt += 1
                    if cnt > m: return False
                    summ = nums[i]
            return True

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mi = (lo + hi) // 2
            if not judge(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
