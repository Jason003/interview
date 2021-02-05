import random


class Block:
    def __init__(self):
        self.address = list(range(1024, 2048))
        self.loc = {n: i for i, n in enumerate(self.address)}
        self.address_info = {}

    def get_unused_block(self):
        if not self.address:
            return None
        return self.address[random.randint(0, len(self.address) - 1)]

    def write(self, info):
        val = self.get_unused_block()
        if val is None:
            return False
        self.address_info[val] = info
        idx = self.loc[val]
        self.loc.pop(val)
        last_value = self.address[-1]
        if idx == len(self.address) - 1:
            self.address.pop()
            return True
        self.loc[last_value] = idx
        self.address[idx] = last_value
        self.address.pop()
        return True

    def delete(self, block):
        self.address.append(block)
        self.loc[block] = len(self.address) - 1

    def getInfo(self, block):
        return self.address_info.get(block, None)


block = Block()
for i in range(1025):
    print(block.write(i))
block.delete(1024)
print(block.write(1))
print(block.write(1))
