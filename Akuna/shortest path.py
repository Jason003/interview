import collections
def shortestPath(edges, start, end):
    graph = collections.defaultdict(set)
    for i, j in edges:
        graph[i].add(j)
    dq = collections.deque([start])
    prev = {} # record previous node in the shortest path
    seen = {start}
    while dq:
        curr = dq.popleft()
        for neigh in graph[curr]:
            if neigh == end:
                prev[end] = curr
                res = []
                while end != start:
                    res.append(end)
                    end = prev[end]
                res.append(start)
                return res[::-1]
            if neigh not in seen:
                seen.add(neigh)
                dq.append(neigh)
                prev[neigh] = curr
    return []

print(shortestPath([[0, 1], [1, 2], [0, 2], [1, 4], [4, 3]], 0, 3))
