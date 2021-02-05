class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
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

    def get(self, key: int) -> int:
        if key not in self.map: return -1
        node = self.map[key]
        self.remove(node)
        self.addAfter(self.head, node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.addAfter(self.head, node)
            node.val = value
        else:
            if self.n == self.capacity:
                toRemove = self.tail.prev
                self.map.pop(toRemove.key)
                self.remove(toRemove)
            else:
                self.n += 1
            toAdd = Node(key, value)
            self.map[key] = toAdd
            self.addAfter(self.head, toAdd)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)