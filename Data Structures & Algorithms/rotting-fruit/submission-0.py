class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use the sophisticated way

        self.fresh = 0
        r = len(grid)
        c = len(grid[0])

        q = deque()
        count = 0

        def multi_bfs(j:int,k:int):
            # do sth
            if 0<=j<r and 0<=k<c:
                if grid[j][k] == 1:
                    # if not rotten
                    q.append([j,k])
                    grid[j][k] = 2
                    self.fresh -= 1
            return
        
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 2:
                    q.append([x,y])
                if grid[x][y] == 1:
                    self.fresh += 1

        # no fresh to rot
        if self.fresh == 0:
            return 0
        # no rotten to rot
        if not q:
            return -1

        while q:
            for i in range(len(q)):
                j,k = q.popleft()
                multi_bfs(j+1,k)
                multi_bfs(j-1,k)
                multi_bfs(j,k+1)
                multi_bfs(j,k-1)
            count += 1
        
        # print(count, self.fresh, grid)

        if self.fresh != 0:
            return -1

        return count-1