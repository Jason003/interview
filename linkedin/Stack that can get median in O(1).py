'''
The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers.
'''
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        return -self.lo[0] if self.n & 1 else (self.hi[0] - self.lo[0]) / 2

class Node:
    def __init__(self, val):
        self.pre = None
        self.nxt = None
        self.val = val

class Stack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

    def push(self, val):
        new_node = Node(val)
        new_node.nxt = self.head
        self.count += 1
        if self.count == 1:
            self.mid = new_node
        else:
            self.head.pre = new_node
            if self.count % 2:
                self.mid = self.mid.pre
        self.head = new_node

    def pop(self):
        if self.count == 0:
            raise Exception('Empty Stack!')
        res = self.head.val
        self.head = self.head.nxt
        if self.head != None:
            self.head.pre = None
        self.count -= 1
        if self.count % 2 == 0:
            self.mid = self.mid.nxt
        return res

    def findMiddle(self):
        if self.count == 0:
            raise Exception('Empty Stack!')
        return self.mid.val



s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(6)
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(s.findMiddle())