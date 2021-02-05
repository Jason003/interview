'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-distance-from-all-buildings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if m==0:
            return -1
        n=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
        cnt=0
        distance=[[0 for i in range(n)] for i in range(m)]
        counts=[[0 for i in range(n)] for i in range(m)]
        min_dist=float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    cnt+=1
                    queue.append((i,j,0))
                    marked=[[False for i in range(n)] for i in range(m)]
                    while queue:
                        cur_i,cur_j,dist=queue.popleft()
                        for direction in directions:
                            new_i=cur_i+direction[0]
                            new_j=cur_j+direction[1]
                            if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j]==0 and not marked[new_i][new_j]:
                                counts[new_i][new_j]+=1
                                distance[new_i][new_j]+=dist+1
                                queue.append((new_i,new_j,dist+1))
                                marked[new_i][new_j]=True
        for i in range(m):
            for j in range(n):
                if counts[i][j]==cnt and distance[i][j]<min_dist:
                    min_dist=distance[i][j]
        return min_dist if min_dist<float('inf') else -1