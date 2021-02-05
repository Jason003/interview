class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        mark = {}
        def color(i, c):
            if i in mark:
                return mark[i] == c
            mark[i] = c
            for j in graph[i]:
                if not color(j, 1 - c):
                    return False
            return True
        for i in range(len(graph)):
            if not color(i, 0) and not color(i, 1):
                return False
        return True