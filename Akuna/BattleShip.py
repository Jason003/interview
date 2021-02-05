import collections, random, copy
class BattleShip:
    def __init__(self, n, ships): # n is the length of row and col, and ships is a list of tuples representing height and width of ships where ship[0] <= ship[1]
        self.n = n
        self.board = [['E'] * n for _ in range(n)]
        self.ships = ships
        self.targets = collections.deque() # once we shot a ship, we will add all the non-visited cells surrounding it to targets
        self.shot = set()
        self.place()

    def _canPlace(self, x, y, ship, dir): # determine if a ship could be placed with (x, y) as upper-left point in dir direction, this method can be used in place and shoot method
        if dir == 0:
            xx, yy = x + ship[0] - 1, y + ship[1] - 1
        else:
            xx, yy = x + ship[1] - 1, y + ship[0] - 1
        return 0 <= xx < self.n and 0 <= yy < self.n and all((i, j) not in self.shot and self.board[i][j] == 'E' for i in range(x, xx + 1) for j in range(y, yy + 1))

    def _notConnected(self, x, y, ship, dir): # this method will be used to determine if we can place a ship here, whether it will touch another ship
        if dir == 0:
            xx, yy = x + ship[0] - 1, y + ship[1] - 1
        else:
            xx, yy = x + ship[1] - 1, y + ship[0] - 1
        for i in range(x, xx + 1):
            for j in (y, yy + 1):
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ii, jj = i + di, j + dj
                    if 0 <= ii < self.n and 0 <= jj < self.n and self.board[ii][jj] != 'E':
                        return False
        for i in (x, xx + 1):
            for j in range(y, yy + 1):
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ii, jj = i + di, j + dj
                    if 0 <= ii < self.n and 0 <= jj < self.n and self.board[ii][jj] != 'E':
                        return False
        return True

    def _placeOneShip(self, x, y, ship, dir, board, id): # determine if a ship could be placed with (x, y) as upper-left point in dir direction, this method can be used in place and shoot method
        if dir == 0:
            xx, yy = x + ship[0] - 1, y + ship[1] - 1
        else:
            xx, yy = x + ship[1] - 1, y + ship[0] - 1
        for i in range(x, xx + 1):
            for j in range(y, yy + 1):
                board[i][j] = str(id)

    def place(self):
        '''
Don't place your ships touching each other
An opponent who scores a hit on your grid will likely circle that point looking for the rest of the ship. If your opponent finds two ships at once, you've just lost an extra ship.

Place asymmetrical.
The human mind seeks patterns. So, don't mirror or copy your ship placements. If you have a ship one square away from both edges in the upper left, don't do the same thing in the lower right because else your opponent will be more likely to find both ships after finding the first one.

Place a ship on the edge of the board.
Many players will fire most of their shots the middle of the board. Having at least one or two ships on an edge may give you an advantage.

But don't place all your ships on the edge as then r your opponent may guess the pattern.

Be unpredictable.
If you and your opponent know each other, use that psychology to your benefit. If she thinks you always place your ships close together, opt for a more spacious layout.

If you have followed the above rules for a few games in a row against the same opponent, break them to confuse your opponent. It's a great way to throw experienced opponents off their game...until they figure out what you're doing.
        :return:
        '''
        # we will traverse the self.ships and place them, and we will use the index to represent a ship in self.board
        for id, ship in enumerate(self.ships):
            seen = set()
            success = False
            for _ in range(1000):
                x, y, dir = random.randint(0, self.n - 1), random.randint(0, self.n - 1), random.randint(0, 1)
                if (x, y, dir) not in seen:
                    seen.add((x, y, dir))
                    if self._canPlace(x, y, ship, dir) and self._notConnected(x, y, ship, dir):
                        self._placeOneShip(x, y, ship, dir, self.board, id)
                        success = True
                        break
            if not success:
                self.board = [['E'] * self.n for _ in range(self.n)]
                self.place()


bs = BattleShip(10, ((1, 5), (2, 6), (1, 7), (2, 8)))
print('\n'.join(map(' '.join, bs.board)))