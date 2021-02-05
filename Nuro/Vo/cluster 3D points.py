import collections


def cluster(points, d):
    n = len(points)

    parent = {i: i for i in range(n)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2 + (
                    points[i][2] - points[j][2]) ** 2 <= d ** 2:
                parent[find(i)] = find(j)

    res = collections.defaultdict(set)
    for i in range(n):
        res[find(i)].add(points[i])
    return res.values()


print(cluster([(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 1, 3), (1, 1, 2), (1, 1, 1), (0, 1, 1), (0, 0, 1), (0, 0, 0)], 1))
