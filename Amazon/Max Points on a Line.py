import collections
class Solution:
    def maxPoints(self, ps):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not ps: return 0
        res, n = 1, len(ps)

        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)

        for i in range(n - 1):
            same, vertical, d = 1, 1, collections.Counter()
            for j in range(i + 1, n):
                p1, p2 = ps[i], ps[j]
                if p1 == p2:
                    same += 1
                    continue
                elif p1[0] == p2[0]:
                    vertical += 1
                    continue
                else:
                    dy, dx = p2[1] - p1[1], p2[0] - p1[0]
                    g = gcd(int(dx), int(dy))
                    dy, dx = dy / g, dx / g
                    d[(dx, dy)] += 1
            res = max(res, (max(d.values()) if d.values() else 0) + same, vertical)
        return res
