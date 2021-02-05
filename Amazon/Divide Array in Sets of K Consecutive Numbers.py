'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.
'''

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        cnt = collections.Counter(nums)
        for i in sorted(nums):
            if cnt[i] > 0:
                for j in range(i, i + k):
                    if cnt[j] <= 0:
                        return False
                    cnt[j] -= 1
        return True