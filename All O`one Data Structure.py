class Node:

    def __init__(self, val):
        self.val = val
        self.pre = None
        self.nxt = None
        self.keySet = set()


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-float('inf'))
        self.tail = Node(float('inf'))
        self.keyCount = {}
        self.countNode = {}
        self.tail.pre = self.head
        self.head.nxt = self.tail

    def _change(self, key, num):
        curCount = self.keyCount[key]
        curNode = self.countNode[curCount]
        self.keyCount[key] += num
        if curCount + num not in self.countNode:
            newNode = Node(curCount + num)
            self.countNode[curCount + num] = newNode
            self._addAfter(curNode if num == 1 else curNode.pre, newNode)
        else:
            newNode = self.countNode[curCount + num]
        newNode.keySet.add(key)
        self._removeKey(curNode, key)

    def _removeKey(self, node, key):
        node.keySet.remove(key)
        if not node.keySet:
            self._removeNode(node)

    def _removeNode(self, node):
        self.countNode.pop(node.val)
        node.pre.nxt, node.nxt.pre = node.nxt, node.pre

    def _addAfter(self, node, toAdd):
        nxt = node.nxt
        toAdd.nxt = nxt
        nxt.pre = toAdd
        toAdd.pre = node
        node.nxt = toAdd

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.keyCount:
            self.keyCount[key] = 1
            if 1 not in self.countNode:
                self._addAfter(self.head, Node(1))
            self.countNode[1] = self.head.nxt
            self.head.nxt.keySet.add(key)
        else:
            self._change(key, 1)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.keyCount: return
        if self.keyCount[key] == 1:
            self._removeKey(self.countNode[1], key)
            self.keyCount.pop(key)
        else:
            self._change(key, -1)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return list(self.tail.pre.keySet)[0] if self.head.nxt != self.tail else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return list(self.head.nxt.keySet)[0] if self.head.nxt != self.tail else ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()