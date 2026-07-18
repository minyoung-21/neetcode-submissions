class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])

        res = []

        pacific = [[False]*c for _ in range(r)]
        atlantic = [[False]*c for _ in range(r)]

        def bfs(source:List[int], ocean:List[int]):
            q = deque(source)

            while q:
                row, col = q.popleft()

                if ocean[row][col]:
                    continue
                else:
                    ocean[row][col] = True

                if 0<=row-1<r and heights[row][col] <= heights[row-1][col]:
                    q.append((row-1, col))
                if 0<=col-1<c and heights[row][col] <= heights[row][col-1]:
                    q.append((row, col-1))
                if 0<=row+1<r and heights[row][col] <= heights[row+1][col]:
                    q.append((row+1, col))
                if 0<=col+1<c and heights[row][col] <= heights[row][col+1]:
                    q.append((row, col+1))

        p = []
        a = []
        
        for i in range(r):
            p.append([i,0]) # first column
            a.append([i,c-1]) # last column
        
        for j in range(c):
            p.append([0,j]) # first row
            a.append([r-1,j]) # last row

        bfs(p, pacific)
        bfs(a, atlantic)

        for x in range(r):
            for y in range(c):
                if pacific[x][y] and atlantic[x][y]:
                    res.append([x,y])
        
        return res