import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        return -self.lo[0] if self.n & 1 else (self.hi[0] - self.lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()