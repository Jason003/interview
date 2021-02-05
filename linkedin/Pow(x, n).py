class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        return self.myPow(x * x, n // 2) if n % 2 == 0 else self.myPow(x, n - 1) * x
