class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r = len(grid)
        c = len(grid[0])
        # checker = [[False]*c for _ in range(r)]
        inf = 2147483647
        q = deque()
        visit = set()

        def multi_bfs(j:int,k:int):
            # do something
            if 0<=j<r and 0<=k<c:
                if grid[j][k] == inf:
                    # checker[j][k] = True
                    q.append([j,k])
                    grid[j][k] = dist + 1
                else:
                    return
            else:
                return
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 0:
                    q.append([x,y])
                    # checker[x][y] = True
        
        dist = 0

        while q:
            for i in range(len(q)):
                j,k = q.popleft()
                grid[j][k] = dist
                multi_bfs(j+1,k)
                multi_bfs(j-1,k)
                multi_bfs(j,k+1)
                multi_bfs(j,k-1)
            dist += 1