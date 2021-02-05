'''
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
'''
import collections
class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0
        station, q, seenSta, step, seenBus = collections.defaultdict(set), collections.deque(), {S}, 0, set()
        for i in range(len(routes)):
            for s in routes[i]:
                station[s].add(i)
        q.append(S)
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                for b in station[cur]:
                    if b not in seenBus:
                        seenBus.add(b)
                        for s in routes[b]:
                            if s not in seenSta:
                                seenSta.add(s)
                                if s == T: return step + 1
                                else: q.append(s)
            step += 1
        return -1