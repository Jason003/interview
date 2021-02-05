import collections
class Solution:
    def accountsMerge(self, accounts):
        owner = {}
        parent = {}
        union = collections.defaultdict(set)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for acc in accounts:
            p = acc[0]
            for email in acc[1:]:
                parent.setdefault(email, email)
                owner[email] = p
                parent[find(email)] = find(acc[1])

        for e in owner:
            union[find(e)].add(e)

        return [[owner[k]] + sorted(list(v)) for k, v in union.items()]