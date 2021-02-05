# -*- coding: utf-8 -*-
# @Time : 2020/12/10 21:27
# @Author : Jiefan

class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        def dfs(idx, t, cur):
            if t == 0:
                res.append(cur)
                return
            if t < 0: return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]: continue # avoid duplication
                dfs(i + 1, t - candidates[i], cur + [candidates[i]])
        res = []
        dfs(0, target, [])
        return res

'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''
# this is different from coin change 2, becaue the order matters here, but for coin change 2, the result of
# the given example is 4

def combinationSum4(nums, target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[-1]

