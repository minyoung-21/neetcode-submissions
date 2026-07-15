class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        checker = [[False]*c for _ in range(r)]

        count = 0

        def dfs(i:int, j:int):
            if 0<=i<r and 0<=j<c:
                # do something
                if grid[i][j] == '1':
                    if checker[i][j] == False:
                        checker[i][j] = True
                        # 
                        dfs(i-1,j)
                        dfs(i,j-1)
                        dfs(i,j+1)
                        dfs(i+1,j)
        
        for x in range(r):
            for y in range(c):
                if checker[x][y] == False and grid[x][y] == '1':
                    dfs(x,y)
                    count += 1
        
        return count