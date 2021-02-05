class Node:
    def __init__(self, index=None, val=None, next = None):
        self.index = index
        self.val = val
        self.next = next

class SparseVector:
    def __init__(self, size):
        self.size = size
        self.head = None

    def set(self, index, val):
        if index >= self.size or index < 0:
            raise Exception('Index out of range: {} of {}'.format(index, self.size))

        if not self.head:
            self.head = Node(index, val)
            return
        prev = Node()
        curr = self.head
        prev.next = curr
        while curr and curr.index < index:
            prev, curr = curr, curr.next
        if curr:
            if curr.index == index:
                curr.val = val
            else:
                prev.next = Node(index, val, curr)
        else:
            prev.next = Node(index, val)
    def get(self, index):
        if index >= self.size or index < 0:
            raise Exception('Index out of range: {} of {}'.format(index, self.size))
        curr = self.head
        while curr:
            if curr.index == index: return curr.val
            curr = curr.next
        return 0.0

    def toString(self):
        l = []
        curr = self.head
        for i in range(self.size):
            if curr and curr.index == i:
                l.append(curr.val)
                curr = curr.next
            else:
                l.append(0.0)
        return '[' + ','.join(map(str, l)) + ']'

    def add(self, v2):
        if self.size != v2.size:
            raise Exception('length mismatch')
        res = []
        for i in range(self.size):
            res.append(self.get(i) + v2.get(i))
        return res

    def dot(self, v2):
        if self.size != v2.size:
            raise Exception('length mismatch')
        res = 0
        for i in range(self.size):
            res += self.get(i) * v2.get(i)
        return res

    def norm(self):
        res = 0
        for i in range(self.size):
            res += self.get(i) * self.get(i)
        return res ** 0.5

    def cos(self, v2):
        return self.dot(v2) / (self.norm() * v2.norm())

v1 = SparseVector(5)
v1.set(0, 4.0)
v1.set(1, 5.0)

v2 = SparseVector(5)
v2.set(1, 2.0)
v2.set(3, 3.0)

v3 = SparseVector(2)
print(v1.add(v2)) #should print [4.0, 7.0, 0.0, 3.0, 0.0]
#print(v1.add(v3)) #error -- vector lengths don’t match

print(v1.dot(v2)) #should print 10
#print(v1.dot(v3)) #error -- vector lengths don’t match

print(v1.cos(v2)) #should print 0.433
#print(v1.cos(v3)) #error -- vector lengths don’t match

v = SparseVector(100) #size constructor size is 100.
v.set(0, 1.0)
v.set(3, 2.0)
v.set(80,-4.5)

print(v.get(80))
print(v.get(50))

try:
    print(v.get(100))
    raise Exception('We should not get here, an exception should have been thrown')
except:
    print('success')


print(v.toString()) #should print something like [1.0, 0.0, 0.