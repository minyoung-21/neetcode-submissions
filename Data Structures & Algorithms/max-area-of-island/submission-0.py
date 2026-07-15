class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        checker = [[False]*c for _ in range(r)]
        max_area = 0

        def count_area(i:int,j:int) -> int:
            # start counting
            # 
            if 0<=i<r and 0<=j<c:
                if checker[i][j] == False and grid[i][j] == 1:
                    checker[i][j] = True
                    
                    return 1 + count_area(i+1,j)+count_area(i-1,j)+count_area(i,j+1)+count_area(i,j-1)
                else:
                    return 0
            else:
                return 0

        
        for x in range(r):
            for y in range(c):
                if checker[x][y] == False and grid[x][y] == 1:
                    
                    max_area = max(max_area,count_area(x,y))

        return max_area