import collections
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dq = collections.deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.dq.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.dq and timestamp - self.dq[0] >= 300:
            self.dq.popleft()
        return len(self.dq)
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [0] * 300
        self.bucket = [0] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300
        if self.time[idx] != timestamp:
            self.time[idx] = timestamp
            self.bucket[idx] = 1
        else:
            self.bucket[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                res += self.bucket[i]
        return res

# if we want to query for more intervals instead of just 5 mins
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = []
        self.loc = {}


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.loc:
            self.loc[timestamp] = len(self.record)
            self.record.append(1)
        else:
            self.record[self.loc[timestamp]] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for t in range(timestamp, timestamp - 300, -1):
            if t in self.loc:
                res += self.record[self.loc[t]]
        return res