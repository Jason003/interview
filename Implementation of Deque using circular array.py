class Deque:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * self.size
        self.front = -1
        self.rear = 0

    def isFull(self):
        return self.front == (self.rear + 1) % self.size

    def isEmpty(self):
        return self.front == -1

    def insertFront(self, val):
        if self.isFull():
            raise Exception('Deque is full')
        if self.isEmpty():
            self.front = 0
        else:
            self.front = (self.front + self.size - 1) % self.size
        self.arr[self.front] = val

    def insertRear(self, val):
        if self.isFull():
            raise Exception('Deque is full')
        if self.isEmpty():
            self.front = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = val

    def deleteFront(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        if self.front == self.rear:
            self.front = -1
            self.rear = 0
        else:
            self.front = (self.front + 1) % self.size

    def deleteRear(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        if self.front == self.rear:
            self.front = -1
            self.rear = 0
        else:
            self.rear = (self.rear - 1 + self.size) % self.size

    def getFront(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            raise Exception('Deque is empty')
        return self.arr[self.rear]







