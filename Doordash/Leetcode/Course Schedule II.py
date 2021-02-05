import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = collections.defaultdict(set)
        is_pre = collections.defaultdict(set)
        for i, j in prerequisites:
            pre[i].add(j)
            is_pre[j].add(i)
        dq = collections.deque([i for i in range(numCourses) if not pre[i]])
        res = []
        while dq:
            curr = dq.popleft()
            res.append(curr)
            for nxt in is_pre[curr]:
                pre[nxt].remove(curr)
                if not pre[nxt]:
                    dq.append(nxt)
        return res if len(res) == numCourses else []