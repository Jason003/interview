import heapq


class Cache:
    def __init__(self, capacity):
        self.heap = []
        self.d = {}
        self.capacity = capacity
        self.time = 0

    def put(self, key, rank):
        # O(n)
        self.time += 1
        if key in self.d:
            self.d[key] = rank
            for i in range(len(self.heap)):
                if self.heap[i][2] == key:
                    self.heap[i] = (rank, self.time, key)
                    heapq.heapify(self.heap)
                    return
        else:
            self.d[key] = rank
            heapq.heappush(self.heap, (rank, self.time, key))
            if len(self.heap) > self.capacity:
                r, t, k = heapq.heappop(self.heap)
                self.d.pop(k)

    def get(self, key):
        return self.d.get(key, -1)

    def print(self):
        print(self.d)

cache = Cache(3)
cache.put(1,1)
cache.print()
cache.put(2,2)
cache.print()
cache.put(3,3)
cache.print()
cache.put(4,2)
cache.print()
cache.put(5,2)
cache.print()
cache.put(6,4)
cache.print()


