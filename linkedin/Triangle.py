'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

class Solution:
    def minimumTotal(self, t) -> int:
        for i in range(1, len(t)):
            for j in range(i + 1):
                if j == 0: t[i][j] += t[i - 1][j]
                elif j == i: t[i][j] += t[i - 1][j - 1]
                else: t[i][j] += min(t[i - 1][j], t[i - 1][j - 1])
        return min(t[len(t) - 1])