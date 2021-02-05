import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if arr[mi][0] == timestamp:
                return arr[mi][1]
            elif arr[mi][0] > timestamp:
                hi = mi - 1
            else:
                lo = mi + 1
        return '' if hi == -1 else arr[hi][1]