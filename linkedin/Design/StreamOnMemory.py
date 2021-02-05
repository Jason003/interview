# -*- coding: utf-8 -*-
# @Time : 2020/12/11 9:22
# @Author : Jiefan

'''
设计一个基于内存的streaming系统，stream以(timestamp, binary_size)的消息进入，然后client会query以ts结束大小为k的内容。
'''
import bisect
class StreamingSystem:
    def __init__(self):
        self.record = []

    def add(self, id, timestamp, size):
        self.record.append((timestamp, id, size))

    def query(self, timestamp, k): # O(log(n) + k / size)
        idx = bisect.bisect(self.record, (timestamp + 1, )) - 1 # if timestamp is an integer
        res = []
        while idx >= 0 and k - self.record[idx][-1] >= 0:
            res.append(self.record[idx])
            idx -= 1
            k -= self.record[idx][-1]
        return res

s = StreamingSystem()
s.add(0,0,1)
s.add(1,1,1)
s.add(2,2,1)
s.add(3,3,1)
s.add(5,4,1)
print(s.query(100, 3))
s.add(10,99,4)
print(s.query(100, 3))


