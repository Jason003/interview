class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != ori or image[x][y] == newColor: return
            image[x][y] = newColor
            for d in ((0,1),(0,-1),(1,0),(-1,0)):
                dfs(x + d[0], y + d[1])
        ori, m, n = image[sr][sc], len(image), len(image[0])
        dfs(sr, sc)
        return image