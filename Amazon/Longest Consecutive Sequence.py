'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, nums = 0, set(nums)
        for n in nums:
            if n - 1 not in nums:
                cnt, nxt = 1, n + 1
                while nxt in nums:
                    cnt, nxt = cnt + 1, nxt + 1
                res = max(res, cnt)
        return res