import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.loc = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.loc: return False
        self.loc[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.loc: return False
        last = self.list[-1]
        if val != last:
            pos = self.loc[val]
            self.loc[last] = pos
            self.list[pos] = last
        self.loc.pop(val)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[random.randint(0, len(self.list) - 1)]