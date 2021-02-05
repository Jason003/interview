class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = [[i ** 2 + j ** 2, i, j] for i, j in points]

        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if points[i][0] < points[r][0]:
                    points[p], points[i] = points[i], points[p]
                    p += 1
            points[r], points[p] = points[p], points[r]
            if p == K - 1:
                return
            elif p > K - 1:
                quickSelect(l, p - 1)
            else:
                quickSelect(p + 1, r)

        quickSelect(0, len(points) - 1)
        return [[i, j] for _, i, j in points[:K]]
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for i, j in points:
            heapq.heappush(heap, (-i * i - j * j, i, j))
            if len(heap) > K:
                heapq.heappop(heap)
        return [(i, j) for _, i, j in heap]