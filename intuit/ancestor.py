import collections
def findNodesWithZeroOrOneParent(edges):
    parent = collections.defaultdict(set)
    allNodes = set()
    for i, j in edges:
        parent[j].add(i)
        allNodes.add(i)
        allNodes.add(j)
    return [k for k in allNodes if len(parent[k]) <= 1]

print(findNodesWithZeroOrOneParent([[1,4], [1,5], [2,5], [3,6], [6,7]]))

def hasCommonAncestor(edges, x, y):
    parent = collections.defaultdict(set)
    for i, j in edges:
        parent[j].add(i)
    def getAllAncestors(x):
        nonlocal parent
        if x not in parent:
            return set()
        res = set(parent[x])
        for p in parent[x]:
            res |= getAllAncestors(p)
        return res
    return len(getAllAncestors(x) & getAllAncestors(y)) > 0
print(hasCommonAncestor([[1,4], [1,5], [2,5], [3,6], [6,7]], 2, 5))

def earliestAncestor(edges, x):
    parent = collections.defaultdict(set)
    for i, j in edges:
        parent[j].add(i)
    dq = collections.deque([x])
    curLayer = []
    seen = {x}
    while dq:
        curLayer = list(dq)
        sz = len(dq)
        for _ in range(sz):
            node = dq.popleft()
            for p in parent[node]:
                if p not in seen:
                    seen.add(p)
                    dq.append(p)
    return curLayer
print(earliestAncestor([[1,4], [1,5], [2,5], [3,6], [6,7], [8,7], [9,8]], 7))
