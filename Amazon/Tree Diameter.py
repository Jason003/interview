'''
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.
'''
import collections
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        dis = {}
        def dfs(node, seen, d):
            dis[node] = d
            for neigh in graph[node]:
                if neigh not in seen:
                    dfs(neigh, seen | {neigh}, d + 1)
        dfs(0, {0}, 0)
        mx = max(dis.values() or [0])
        idx = [i for i in dis if dis[i] == mx][0]
        dis = {}
        dfs(idx, {idx}, 0)
        return max(dis.values() or [0])

