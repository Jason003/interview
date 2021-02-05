# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

class Solution:
    def findCelebrity(self, n: int) -> int:
        res = 0
        for i in range(n):
            if knows(res, i):
                res = i
        for i in range(n):
            if i == res: continue
            if knows(res, i) or not knows(i, res): return -1
        return res