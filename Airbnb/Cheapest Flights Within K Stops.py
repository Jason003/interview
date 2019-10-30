import collections
import heapq

class Solution:

    def findCheapestPrice(self, flights, src, dst, K):
        '''
        no cycle detection, because we can only move K steps, there will not be a circle problem
        '''
        graph = collections.defaultdict(dict)
        for s, e, cost in flights:
            graph[s][e] = cost
        heap = [(0, src, K + 1)]
        while heap:
            cost, curr, stops = heapq.heappop(heap)
            if curr == dst:
                return cost
            if stops:
                for nxt, price in graph[curr].items():
                    heapq.heappush(heap, (cost + price, nxt, stops - 1))
        return -1

        # # bellman ford
        # dp = [[float("inf")] * (K + 2) for _ in range(n)]
        # dp[src] = [0] * (K + 2)
        # for k in range(1, K + 2):
        #     for u, v, w in flights:
        #         if dp[u][k - 1] != float('inf') and dp[u][k - 1] + w < dp[v][k]: dp[v][k] = dp[u][k - 1] + w
        # return dp[dst][K + 1] if dp[dst][K + 1] != float('inf') else -1

    def findCheapestPrice_optimized(self, flights, src, dst, K):
        '''
        used a dictionary to track the number of movies it took to reach a node,
        and then i only visit the node again if the current path took fewer moves
        to reach the node than any previous path.
        '''
        graph = collections.defaultdict(dict)
        for s, e, cost in flights:
            graph[s][e] = cost
        heap = [(0, src, 0)]
        seen = {} # city : steps
        while heap:
            cost, curr, steps = heapq.heappop(heap)
            if curr == dst:
                return cost
            if curr in seen and seen[curr] < steps: # if
                continue
            seen[curr] = steps
            if steps <= K:
                for nxt, price in graph[curr].items():
                    heapq.heappush(heap, (cost + price, nxt, steps + 1))
        return -1