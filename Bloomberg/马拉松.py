class Node():
    def __init__(self, person):
        self.person = person
        self.next = None
        self.prev = None


class Marrathon():
    def __init__(self, numSensor):
        self.sensorsHead = [0] * numSensor
        self.sensorsTail = [0] * numSensor
        self.person2Node = dict()
        for i in range(numSensor):
            self.head = Node(-1)
            self.tail = Node(-1)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.sensorsHead[i] = self.head
            self.sensorsTail[i] = self.tail

    def update(self, person, sensor):
        if person in self.person2Node:
            node = self.person2Node[person]
            self.removeNode(node)
            self.addNode(sensor, node)
        else:  # person 1st time appear
            node = Node(person)
            self.person2Node[person] = node
            self.addNode(sensor, node)

    def addNode(self, sensor, node):
        tail = self.sensorsTail[sensor]
        p = tail.prev
        p.next = node
        node.next = tail
        tail.prev = node
        node.prev = p

    def removeNode(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def topK(self, k):
        res = []

        for i in range(len(self.sensorsHead) - 1, -1, -1):
            if k == 0:
                break
            candidate = self.sensorsHead[i].next
            while candidate.person != -1 and k > 0:
                res.append(candidate.person)
                k -= 1
                candidate = candidate.next
        return res

m = Marrathon(5)
m.update(1, 1)
m.update(1, 2)
m.update(1, 3)
m.update(2, 1)
m.update(2, 4)
m.update(3, 1)
print(m.topK(2))