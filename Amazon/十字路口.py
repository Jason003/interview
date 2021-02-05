import collections

class CrossRoad:
    def __init__(self):
        self.crossRoads = collections.defaultdict(collections.deque)
        self.t = 0

    def arrival(self, carId, roadId, directionId): # road id is one from 'N', 'S', 'E', 'W'
        self.crossRoads[roadId].append((self.t, carId, directionId))
        self.t += 1

    def departure(self):
        roadId, minT = None, float('inf')
        for r in self.crossRoads:
            if self.crossRoads[r] and self.crossRoads[r][0][0] < minT:
                roadId = r
                minT = self.crossRoads[r][0][0]
        if roadId == None:
            return None
        t, carId, directionId = self.crossRoads[roadId].popleft()
        if directionId != roadId:
            self.arrival(carId, directionId, directionId)
        return carId, roadId, directionId

cr = CrossRoad()
cr.arrival(0, 'N', 'S')
print(cr.departure())
cr.arrival(1, 'S', 'N')
cr.arrival(2, 'W', 'E')
cr.arrival(3, 'E', 'W')

print(cr.departure())
print(cr.departure())
print(cr.departure())
print(cr.departure())
print(cr.departure())
print(cr.departure())
print(cr.departure())
