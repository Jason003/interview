import collections

def removeNodeFromBT(treeList, node):
    tree = collections.defaultdict(set)
    for parent, child in treeList:
        tree[parent].add(child)
    dq = collections.deque([node])
    toRemove = {node}
    while dq:
        curr = dq.popleft()
        for child in tree[curr]:
            if child not in toRemove:
                toRemove.add(child)
                dq.append(child)
    return [edge for edge in treeList if edge[0] not in toRemove and edge[1] not in toRemove]

print(removeNodeFromBT([[1,2],[1,3],[3,4]], 3))
