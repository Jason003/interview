'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y, d = 0, 0, 0
        for c in instructions:
            if c == 'G': x, y = x + dirs[d][0], y + dirs[d][1]
            elif c == 'L': d = (d + 3) % 4
            else: d = (d + 1) % 4
        return (x, y) == (0, 0) or d != 0