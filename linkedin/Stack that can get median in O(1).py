'''
The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers.
'''
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