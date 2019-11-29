'''
Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
'''
class Solution:
    def exclusiveTime(self, n: int, logs):
        res = [0] * n
        stack = []
        pre = 0
        for log in logs:
            i, flag, t = log.split(':')
            i, t = int(i), int(t)
            if stack:
                res[stack[-1]] += t - pre
            pre = t
            if flag == 'start':
                stack.append(i)
            else:
                res[stack.pop()] += 1
                pre += 1
        return res
