'''
Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
'''
import heapq
class Solution:
    def maxEvents(self, events) -> int:
        heap = [] # potential meetings we might be able to attend
        i = 0
        events.sort()
        n = len(events)
        res = 0
        for d in range(1, max(max(e) for e in events) + 1): # traverse all days
            while i < n and events[i][0] <= d: # add meetings we might be able to attend
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < d: # remove meetings we can not attend
                heapq.heappop(heap)
            if heap: # find the meeting we can attend for day d
                heapq.heappop(heap)
                res += 1
        return res