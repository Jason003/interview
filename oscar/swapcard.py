import time
class SwipCard:
    def __init__(self):
        self.lastTime = {}
    def swip(self, id):
        currTime = time.time()
        if id not in self.lastTime:
            self.lastTime[id] = currTime
            return True
        else:
            if currTime - self.lastTime[id] < 1:
                return False
            else:
                self.lastTime[id] = currTime
                return True

sc = SwipCard()
print(sc.swip(1))
time.sleep(1)
print(sc.swip(1))
time.sleep(1)
print(sc.swip(1))
time.sleep(1)
print(sc.swip(1))