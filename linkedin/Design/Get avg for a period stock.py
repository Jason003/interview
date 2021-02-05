import time
import collections


class StockMetrics:
    def __init__(self):
        record_5m = collections.defaultdict(collections.deque)  # {stock_id : [(timestamp, stock_price)]}
        record_1h = collections.defaultdict(collections.deque)
        record_24h = collections.defaultdict(collections.deque)
        sum_5m = collections.Counter()
        sum_1h = collections.Counter()
        sum_24h = collections.Counter()
        self.interval_record = {300: [record_5m, sum_5m], 3600: [record_1h, sum_1h], 86400: [record_24h, sum_24h]}

    def _remove(self, stock_id, currentTime):  # amortized O(1)
        for interval, records in self.interval_record.items():
            record, sum = records
            while record[stock_id] and currentTime - record[stock_id][0][0] > interval:
                sum[stock_id] -= record[stock_id].popleft()[1]

    def add(self, stock_id, price):
        currentTime = time.time()
        self._remove(stock_id, currentTime)
        for interval, records in self.interval_record.items():
            record, sum = records
            record[stock_id].append((currentTime, price))
            sum[stock_id] += price

    def get_avg(self, stock_id, interval):
        if interval not in self.interval_record:
            raise Exception('Invalid interval')
        currentTime = time.time()
        self._remove(stock_id, currentTime)
        numberOfPrices = len(self.interval_record[interval][0][stock_id])
        if numberOfPrices == 0:
            raise Exception('No price record for the stock')
        return self.interval_record[interval][1][stock_id] / numberOfPrices


s = StockMetrics()
s.add(1, 100)
time.sleep(1)
s.add(1, 200)
s.add(1, 300)
s.add(2, 100)
s.add(3, 100)
print(s.get_avg(1, 1))
time.sleep(1)
print(s.get_avg(1, 1))
print(s.get_avg(2, 1))
print(s.get_avg(3, 1))
