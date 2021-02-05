import collections
class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.pre = self.tail, self.head
        self.cnt = collections.Counter(nums)
        self.val2node = {}
        for num in nums:
            if self.cnt[num] == 1:
                self.addNode(self.tail.pre, Node(num))
                self.val2node[num] = self.tail.pre

    def addNode(self, pre, node):
        nxt = pre.next
        node.next = nxt
        nxt.pre = node
        node.pre = pre
        pre.next = node

    def removeNode(self, node):
        node.pre.next, node.next.pre = node.next, node.pre

    def showFirstUnique(self) -> int:
        return -1 if self.head.next == self.tail else self.head.next.val

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        if self.cnt[value] == 1:
            self.addNode(self.tail.pre, Node(value))
            self.val2node[value] = self.tail.pre
        else:
            if value in self.val2node:
                self.removeNode(self.val2node[value])
                self.val2node.pop(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)