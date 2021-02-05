'''
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
'''
import collections
class SnakeGame:

    def __init__(self, width: int, height: int, food):
        self.snake = collections.deque([(0, 0)])
        self.head = (0, 0)
        self.foods = collections.deque(food)
        self.width = width
        self.height = height
        self.score = 0
        self.snakeSet = {(0, 0)}

    def move(self, direction: str) -> int:
        x, y = self.head
        if direction == 'U':
            x -= 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1
        elif direction == 'D':
            x += 1
        if x < 0 or y < 0 or x > self.height - 1 or y > self.width - 1:
            return -1

        self.head = (x, y)
        self.snake.appendleft(self.head)
        if self.foods and self.head == tuple(self.foods[0]):
            self.score += 1
            self.foods.popleft()
        else:
            self.snakeSet.discard(self.snake.pop())
        if self.head in self.snakeSet:
            return -1
        self.snakeSet.add(self.head)
        return self.score