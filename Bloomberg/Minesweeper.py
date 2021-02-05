class MineSweeper:
    def __init__(self, board):
        '''
        if we click 'M', change it to 'X'
        if we click an empty cell 'E'
          (1) if it has no adjacent mine, change it to 'C' and all the unchecked cells should be checked recursively
          (2) if it has one or more adjacent mines, change it to the number of mines around it
        '''
        self.board = board
        
    def updateBoard(self, point):
        """
        :type board: List[List[str]]
        :type point: List[int]
        :rtype: List[List[str]]
        """
        dirs, m, n = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]], len(self.board), len(self.board[0])
        def count(x, y):
            res = 0
            for d in dirs:
                xx, yy = x + d[0], y + d[1]
                if xx >= 0 and yy >= 0 and xx < m and yy < n and self.board[xx][yy] == 'M': res += 1
            return res            
        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n: return
            if self.board[x][y] == 'E':
                c = count(x, y)
                if c == 0:
                    self.board[x][y] = 'C'
                    for d in dirs:
                        dfs(x + d[0], y + d[1])
                else:
                    self.board[x][y] = str(c)
        if self.board[point[0]][point[1]] == 'M': 
            self.board[point[0]][point[1]] = 'X'
            return self.board
        dfs(point[0], point[1])
        return self.board