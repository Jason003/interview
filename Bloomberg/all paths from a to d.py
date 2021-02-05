import collections
def all_paths(edges, start, end):
    res = []
    graph = collections.defaultdict(set)
    for s, e in edges:
        graph[s].add(e)

    def helper(curr, path, seen):
        if curr == end:
            res.append(path + [curr])
            return
        for nei in graph[curr]:
            if nei not in seen:
                helper(nei, path + [curr], seen | {curr})

    helper(start, [], set())
    return res

edges = [(1, 2), (1, 3), (2, 3), (4, 1), (1, 4), (4, 5)]
print(all_paths(edges, 1, 5))
