import collections
import heapq
import copy

class Solution:
    def findCheapestPrice_bellman(self, n, flights, src, dst, K):
        # bellman ford
        dp = collections.defaultdict(dict)
        allCities = {i for i, j, k in flights} | {j for i, j, k in flights}
        # we could do K + 1 times loop, every time, we could relax a node (find the shortest distance between a node with src)
        for city in allCities:
            for k in range(K + 2):
                if city != src:
                    dp[city][k] = float('inf')
                else:
                    dp[city][k] = 0
        prev = {}
        for k in range(1, K + 2):
            for u, v, w in flights:
                if dp[u][k - 1] != float('inf') and dp[u][k - 1] + w < dp[v][k]:
                    dp[v][k] = dp[u][k - 1] + w
                    prev[v] = u
        if dp[dst][K + 1] == float('inf'):
            return 'impossible!'
        else:
            path = [dst]
            while path[-1] != src:
                path.append(prev[path[-1]])
            path = list(map(str, path))[::-1]
            return ' -> '.join(path) + ':' + str(dp[dst][K + 1])

    def findCheapestPrice_bellman_optimized(self, n, flights, src, dst, K):
        # bellman ford
        dp = collections.defaultdict(lambda : float('inf'))
        dp[src] = 0
        prev = {}
        for k in range(1, K + 2):
            tep = copy.deepcopy(dp)
            for u, v, w in flights:
                if dp[u] != float('inf') and dp[u] + w < tep[v]:
                    tep[v] = dp[u] + w
                    prev[v] = u
            dp = tep
        if dp[dst] == float('inf'):
            return 'impossible!'
        else:
            path = [dst]
            while path[-1] != src:
                path.append(prev[path[-1]])
            path = list(map(str, path))[::-1]
            return ' -> '.join(path) + ':' + str(dp[dst])

    def findCheapestPrice_bellman_1d(self, flights, src, dst, K, n):
        # bellman ford
        dp = [float("inf")] * n
        dp[src] = 0
        for k in range(K + 1):
            tep = dp[:]
            for u, v, w in flights:
                if dp[u] != float('inf') and dp[u] + w < tep[v]:
                    tep[v] = dp[u] + w
            dp = tep
        return dp[dst] if dp[dst] != float('inf') else -1

    def findCheapestPrice(self,n, flights, src, dst, K):
        '''
        no cycle detection, because we can only move K steps, there will not be a circle problem
        '''
        graph = collections.defaultdict(dict)
        for s, e, cost in flights:
            graph[s][e] = cost
        heap = [(0, src, None, K + 1)]
        prev = {}
        while heap:
            cost, curr, pre, stops = heapq.heappop(heap)
            prev[curr] = pre
            if curr == dst:
                # incorrect, can not using this to print the route!!!
                path = [dst]
                while path[-1] != src:
                    path.append(prev[path[-1]])
                path = list(map(str, path))[::-1]
                return ' -> '.join(path) + ':' + str(cost)
            if stops:
                for nxt, price in graph[curr].items():
                    heapq.heappush(heap, (cost + price, nxt, curr, stops - 1))
        return -1


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
        seen = {}  # city : steps
        while heap:
            cost, curr, steps = heapq.heappop(heap)
            if curr == dst:
                return cost
            if curr in seen and seen[curr] < steps:  # if
                continue
            seen[curr] = steps
            if steps <= K:
                for nxt, price in graph[curr].items():
                    heapq.heappush(heap, (cost + price, nxt, steps + 1))
        return -1

    def findCheapestPrice_dfs(self, n, flights, src, dst, K):
        # dfs
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        self.res = float('inf')

        def dfs(curr, cost, k, seen):
            if k < 0 or cost >= self.res or curr in seen:
                return
            if curr == dst:
                self.res = min(self.res, cost)
                return
            for nxt, add_cost in graph[curr].items():
                dfs(nxt, cost + add_cost, k - 1, seen | {curr})

        dfs(src, 0, K + 1, set())
        return self.res if self.res != float('inf') else -1


def shortest_path(edges, src, dst, n):
    # bellman ford
    dp = [[float("inf")] * (n + 1) for _ in range(n)]
    dp[src] = [0] * (n + 1)
    for k in range(1, n + 1):
        for u, v, w in edges: # vertex u, vertex v and weight of edge (u, v)
            if dp[u][k - 1] != float('inf') and dp[u][k - 1] + w < dp[v][k]:
                dp[v][k] = dp[u][k - 1] + w
    return dp[dst][n]

print(Solution().findCheapestPrice_bellman_optimized(5,
[[1,2,200],[2,3,250],[1,3,400],[1,4,500],[3,4,50]],
1,
4,
1))
print(Solution().findCheapestPrice(5,
[[1,2,200],[2,3,250],[1,3,400],[1,4,500],[3,4,50]],
1,
4,
1))