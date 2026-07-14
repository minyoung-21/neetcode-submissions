class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        res = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    res += (i - 1 < 0 or grid[i-1][j] == 0) # top
                    res += (i + 1 >= r or grid[i+1][j] == 0) # bottom
                    res += (j + 1 >= c or grid[i][j+1] == 0) # right
                    res += (j - 1 < 0 or grid[i][j-1] == 0) # left
        
        return res