'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.



Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
'''

import functools
class Solution:

    def minDifficulty(self, A, d):
        n = len(A)
        if n < d: return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)