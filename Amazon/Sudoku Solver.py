class Solution:
    def isValidSudoku(self, board: List[List[str]], x, y) -> bool:
        for i in range(9):
            if board[i][y] == board[x][y] and i != x or board[x][i] == board[x][y] and i != y:
                return False
        cnt = 0
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for j in range(y // 3 * 3, y // 3 * 3 + 3):
                if board[i][j] == board[x][y]: cnt += 1
        return cnt == 1
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(i, j):
            if i == 9: return True
            if j == 9: return helper(i + 1, 0)
            if board[i][j] != '.': return helper(i, j + 1)
            for num in range(1, 10):
                board[i][j] = str(num)
                if self.isValidSudoku(board, i, j) and helper(i, j + 1): return True
                board[i][j] = '.'
            return False
        helper(0, 0)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [set() for _ in range(n)]
        col = [set() for _ in range(n)]
        box = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                c = board[i][j]
                if c != '.':
                    if c in row[i] or c in col[j] or c in box[i // 3 * 3 + j // 3]:
                        return False
                    row[i].add(c)
                    col[j].add(c)
                    box[i // 3 * 3 + j // 3].add(c)
        return True