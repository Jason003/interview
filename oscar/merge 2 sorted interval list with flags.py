
# Definition of Interval.
class Interval(object):
    def __init__(self, start, end, flag):
        self.start = start
        self.end = end
        self.flag = flag
    def __str__(self):
        return str(self.start) + ',' + str(self.end) + ',' + str(self.flag)

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        i, j = 0, 0
        intervals = []
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(intervals, list1[i])
                i += 1
            else:
                self.push_back(intervals, list2[j])
                j += 1
        while i < len(list1):
            self.push_back(intervals, list1[i])
            i += 1
        while j < len(list2):
            self.push_back(intervals, list2[j])
            j += 1

        return [i for i in intervals if i.start != i.end]

    def push_back(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return

        last_interval = Interval(intervals[-1].start, intervals[-1].end, intervals[-1].flag)
        if last_interval.end <= interval.start:
            intervals.append(interval)
            return

        if last_interval.end <= interval.end:
            intervals[-1].end = interval.start
            intervals.append(Interval(interval.start, last_interval.end, interval.flag and last_interval.flag))
            intervals.append(Interval(last_interval.end, interval.end, interval.flag))
        else:
            intervals[-1].end = interval.start
            interval.flag = last_interval.flag and interval.flag
            intervals.append(interval)
            intervals.append(Interval(interval.end, last_interval.end, last_interval.flag))

sol = Solution()
for i in sol.mergeTwoInterval([Interval(-float('inf'), 2, False), Interval(2,5,True), Interval(5,10,True), Interval(10,float('inf'),False)], [Interval(-float('inf'), 4, True), Interval(4, float('inf'), True)]):
    print(i)
for i in sol.mergeTwoInterval([Interval(-float('inf'), 45, True), Interval(45,89,False), Interval(89,float('inf'),False)], [Interval(-float('inf'), 67, True), Interval(67, float('inf'), False)]):
    print(i)