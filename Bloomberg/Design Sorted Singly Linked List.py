class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class SortedList:
    def __init__(self):
        self.head = Node()

    def insert(self, val):
        pre = self.head
        cur = self.head.next
        while cur:
            if cur.val >= val:
                break
            pre, cur = cur, cur.next
        if cur and cur.val == val: return
        newNode = Node(val, cur)
        pre.next = newNode

    def print(self):
        cur = self.head.next
        while cur:
            print(cur.val)
            cur = cur.next

s = SortedList()
s.insert(1)
s.insert(1)
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(2)
s.insert(100)
s.insert(0)
s.print()