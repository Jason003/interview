# we can use double linked list and two maps to deal with this problem
class Node:
    def __init__(self, key, val):
        self.key, self.val, self.pre, self.nxt, self.freq = key, val, None, None, 1


class Dll:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.pre = self.head
        self.head.nxt = self.tail

    def add(self, toAdd):
        nxt = self.head.nxt
        nxt.pre = toAdd
        toAdd.nxt = nxt
        toAdd.pre = self.head
        self.head.nxt = toAdd
        self.size += 1

    def remove(self, node):
        node.pre.nxt, node.nxt.pre, self.size = node.nxt, node.pre, self.size - 1

    def pop(self):
        if self.size > 0:
            node = self.tail.pre
            self.remove(node)
            return node
        return None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}
        self.freq_dll = {}
        self.min = None
        self.size = 0

    def _update(self, node):  # add freq by 1
        old_list = self.freq_dll[node.freq]
        old_list.remove(node)
        if node.freq == self.min and old_list.size == 0: self.min += 1
        node.freq += 1
        if node.freq not in self.freq_dll:
            self.freq_dll[node.freq] = Dll()
        self.freq_dll[node.freq].add(node)

    def get(self, key: int) -> int:
        if key in self.key_node:
            node = self.key_node[key]
            self._update(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self._update(node)
        else:
            node = Node(key, value)
            self.key_node[key] = node
            if self.size == self.capacity:
                lastList = self.freq_dll[self.min]
                self.key_node.pop(lastList.pop().key)
                self.size -= 1
            self.size += 1
            self.min = 1
            if 1 not in self.freq_dll: self.freq_dll[1] = Dll()
            self.freq_dll[1].add(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)