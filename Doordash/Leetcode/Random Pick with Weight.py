import random, bisect


class Solution:

    def __init__(self, w: List[int]):
        self.A = [0]
        for num in w:
            self.A.append(self.A[-1] + num)

    def pickIndex(self) -> int:
        num = random.randint(0, self.A[-1] - 1)
        return bisect.bisect_left(self.A, num + 1) - 1