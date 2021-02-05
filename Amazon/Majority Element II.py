'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n1, n2, cnt1, cnt2 = nums[0], nums[0], 0, 0
        for num in nums:
            if num == n1:
                cnt1 += 1
            elif num == n2:
                cnt2 += 1
            elif cnt1 == 0:
                n1 = num
                cnt1 = 1
            elif cnt2 == 0:
                n2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = cnt2 = 0
        for num in nums:
            if num == n1:
                cnt1 += 1
            if num == n2:
                cnt2 += 1
        res = []
        if cnt1 > len(nums) // 3: res.append(n1)
        if cnt2 > len(nums) // 3 and n1 != n2:
            res.append(n2)
        return res