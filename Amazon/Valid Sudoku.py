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