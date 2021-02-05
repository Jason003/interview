import collections, bisect
class StockRecord:
    def __init__(self):
        self.record = collections.defaultdict(list)

    def addStock(self, name, time, amount):
        self.record[name].append((time, amount))

    def query(self, name, time):
        idx = bisect.bisect_left(self.record[name], (time + 1, -1)) - 1
        return -1 if idx == -1 else self.record[name][idx][1]

sr = StockRecord()
sr.addStock("appl", 1, 10)
sr.addStock("appl", 2, 5)
sr.addStock("appl", 4, 8)

print(sr.query("app", 5))