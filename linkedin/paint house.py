# dynamic programming
class Solution:
    def minCostII(self, costs) -> int:
        if not costs:
            return 0
        m, n = len(costs), len(costs[0])
        first, second = None, None
        for i in range(m):
            # store the top 2 choices and corresponding costs for next round
            nxtfirst, nxtsecond = (-1, float('inf')), (-1, float('inf')) # (color, cost)
            for j in range(n):
                if i == 0:
                    if costs[i][j] < nxtfirst[1]:
                        nxtsecond = nxtfirst
                        nxtfirst = (j, costs[i][j])
                    elif costs[i][j] < nxtsecond[1]:
                        nxtsecond = (j, costs[i][j])
                else:
                    if j != first[0]:
                        costs[i][j] += first[1]
                    else:
                        costs[i][j] += second[1]
                    if costs[i][j] < nxtfirst[1]:
                        nxtsecond = nxtfirst
                        nxtfirst = (j, costs[i][j])
                    elif costs[i][j] < nxtsecond[1]:
                        nxtsecond = (j, costs[i][j])
            first = nxtfirst
            second = nxtsecond
        return min(costs[-1])