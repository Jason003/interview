'''
经典地铁题，原题解法就不说了，地里也有很多资源。 主要讲下follow up。
国女问了哪些edge case可以导致error， 我说了两种，一是check out的时候id在map中不存在，
二是check out的时候id对应的时间t大于之前之前check in时的时间。国女表示满意，
又问了运行过程中可能出现哪些情况导致地铁出问题。我说可能有些check in了但是把地铁卡弄丢了没有checkout，
id在memory中积压了很多最后导致memory不够。 解决方法是定期检查已经存储的数据，
如果start time间隔很久的就可以直接remove。
三哥也问了一个follow up，因为我在check out的map里存的是route， 如果之后需要该站点名怎么办。
我说在route里可以用station id，然后单独建一个station name到station id的map，三哥表示满意。

'''
import collections
class UndergroundSystem:

    def __init__(self):
        self.station_time, self.user = collections.defaultdict(list), {}

    def checkIn(self, id, stationName, t):
        self.user[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        self.station_time[self.user[id][0], stationName].append(t - self.user[id][1])

    def getAverageTime(self, startStation, endStation):
        return sum(self.station_time[startStation, endStation]) / len(self.station_time[startStation, endStation])