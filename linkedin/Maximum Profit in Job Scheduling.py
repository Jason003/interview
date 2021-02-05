class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        event = sorted([(startTime[i], endTime[i], profit[i]) for i in range(n)], key=lambda x: x[1])
        dp = [c for a, b, c in event]
        res = 0
        for i in range(n):
            for j in range(i):
                if event[j][1] <= event[i][0]:
                    dp[i] = max(dp[i], dp[j] + event[i][2])
            res = max(res, dp[i])
        return res

'''
Sort the jobs by endTime.

dp[time] = profit means that within the first time duration,
we cam make at most profit money.
Intial dp[0] = 0, as we make profit = 0 at time = 0.

For each job = [s, e, p], where s,e,p are its start time, end time and profit,
Then the logic is similar to the knapsack problem.
If we don't do this job, nothing will be changed.
If we do this job, binary search in the dp to find the largest profit we can make before start time s.
So we also know the maximum cuurent profit that we can make doing this job.

Compare with last element in the dp,
we make more money,
it worth doing this job,
then we add the pair of [e, cur] to the back of dp.
Otherwise, we'd like not to do this job.
'''


def jobScheduling(self, startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]