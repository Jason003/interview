# 1D
def candyCrush1D(candies):
    stack = []
    for c in candies:
        if len(stack) >= 2 and stack[-1] == stack[-2] == c:
            stack.pop()
            stack.pop()
        else:
            stack.append(c)
    return stack
print(candyCrush1D([1,1,2,2,2,1,1,3,3,3]))


class Solution:
    def candyCrush(self, A):
        if not A: return A
        m, n = len(A), len(A[0])
        todo = False
        for i in range(m):
            for j in range(n - 2):
                if abs(A[i][j]) == abs(A[i][j + 1]) == abs(A[i][j + 2]) != 0:
                    A[i][j] = A[i][j + 1] = A[i][j + 2] = -abs(A[i][j])
                    todo = True

        for j in range(n):
            for i in range(m - 2):
                if abs(A[i][j]) == abs(A[i + 1][j]) == abs(A[i + 2][j]) != 0:
                    A[i][j] = A[i + 1][j] = A[i + 2][j] = -abs(A[i][j])
                    todo = True

        for j in range(n):
            k = m - 1
            for i in range(m - 1, -1, -1):
                if A[i][j] > 0:
                    A[k][j] = A[i][j]
                    k -= 1
            for i in range(k, -1, -1):
                A[i][j] = 0

        return self.candyCrush(A) if todo else A