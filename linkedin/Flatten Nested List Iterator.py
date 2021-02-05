import collections
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.dq = collections.deque(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.dq.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.dq and not self.dq[0].isInteger():
            for i in self.dq.popleft().getList()[::-1]:
                self.dq.appendleft(i)
        return len(self.dq) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
class NestedIterator2:
    def __init__(self, nestedList):
        def helper(item):
            for x in item:
                if not x.isInteger():
                    for xx in helper(x.getList()):
                        yield xx
                else:
                    yield x.getInteger()

        self.gen = helper(nestedList)

    def next(self):
        return self.item

    def hasNext(self):
        self.item = next(self.gen, None)
        return self.item != None

class NestedIterator3:
    def __init__(self, nestedList):
        self.mList = nestedList
        self.mIndex = 0 # record the index for the mList we are currently at
        self.mIter = None # none if current ni is integer, not none if current ni is list

    def next(self):
        if self.mIter:
            return self.mIter.next()
        res = self.mList[self.mIndex].getInteger()
        self.mIndex += 1
        return res

    def hasNext(self):
        if self.mIter: # the current ni is a list
            if self.mIter.hasNext():
                return True
            self.mIter = None # the list ends (mIter doesn't have next), we need to set mIter to none and move mIndex
            self.mIndex += 1
        while self.mIndex < len(self.mList):
            ni = self.mList[self.mIndex]
            if ni.isInteger():
                self.mIter = None
                return True
            self.mIter = NestedIterator3(ni.getList())
            if self.mIter.hasNext():
                return True
            self.mIndex += 1
        return False
                