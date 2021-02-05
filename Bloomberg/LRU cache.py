class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.map = {}
        self.n = 0

    def addAfter(self, node, toAdd):
        nxt = node.next
        toAdd.next = nxt
        nxt.prev = toAdd
        toAdd.prev = node
        node.next = toAdd

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self):
        curr = self.head.next
        res = []
        while curr != self.tail:
            res.append(curr.val)
            curr = curr.next
        return res

    def put(self, val) -> None:
        if val in self.map:
            node = self.map[val]
            self.remove(node)
            self.addAfter(self.head, node)
        else:
            if self.n == self.capacity:
                toRemove = self.tail.prev
                self.map.pop(toRemove.val)
                self.remove(toRemove)
            else:
                self.n += 1
            toAdd = Node(val)
            self.map[val] = toAdd
            self.addAfter(self.head, toAdd)
lru = LRUCache(3)
lru.put(1)
lru.put(2)
lru.put(3)
lru.put(4)
lru.put(1)
lru.put(10)
print(lru.get())