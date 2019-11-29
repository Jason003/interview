class Intervals:
    def __init__(self):
        self.A = []
        self.coveredLength = 0

    def insert(self, interval):
        left, right = [], []
        length = 0
        for i in self.A:
            if i[0] > interval[1]:
                right.append(i)
                length += i[1] - i[0]
            elif i[1] < interval[0]:
                left.append(i)
                length += i[1] - i[0]
            else:
                interval[0] = min(interval[0], i[0])
                interval[1] = max(interval[1], i[1])
        self.A = left + [interval] + right
        self.coveredLength = length + interval[1] - interval[0]

    def getCoveredLength(self):
        return self.coveredLength


intervals = Intervals()
intervals.insert([1, 5])
intervals.insert([3, 8])
print(intervals.getCoveredLength())
intervals.insert([8, 10])
print(intervals.getCoveredLength())
intervals.insert([50, 100])
print(intervals.getCoveredLength())
