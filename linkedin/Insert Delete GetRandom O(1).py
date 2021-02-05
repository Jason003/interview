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

    def deleteRandom(self):
        if self.list:
            self.remove(self.getRandom())

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# follow up: what if duplicate is allowed?
import collections
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(set)
        self.num = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = val not in self.d
        self.d[val].add(len(self.num))
        self.num.append(val)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        # swap the value and last number in the array, and then remove the last number
        if val not in self.d or not self.d[val]: return False
        n = len(self.num)
        if n - 1 in self.d[val]:
            self.d[val].remove(n - 1)
            self.num.pop()
            return True
        idx = next(iter(self.d[val]))
        self.d[val].remove(idx)
        last = self.num[-1]
        self.num[idx] = last
        self.d[last].remove(len(self.num) - 1)
        self.d[last].add(idx)
        self.num.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.num[random.randint(0, len(self.num) - 1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()