class Solution:
    def twoCitySchedCost(self, costs) -> int:
        A, B = [], []
        for a, b in costs:
            if a > b:
                B.append(b)
            elif b > a:
                A.append(a)
        temp = sum(map(min, costs))
        if len(A) == len(B):
            return temp
        elif len(A) > len(B):
            return sum(sorted([b - a for a, b in costs if b > a])[:(len(A) - len(B)) // 2]) + temp
        else:
            return sum(sorted([a - b for a, b in costs if a > b])[:(len(B) - len(A)) // 2]) + temp
