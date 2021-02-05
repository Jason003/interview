'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s //= 2
        dp = [([True] + [False] * s) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            dp[i][0] = 1
            for j in range(1, s + 1):
                dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1] else False)
        return dp[-1][-1]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s //= 2
        dp = [True] + [False] * s
        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]