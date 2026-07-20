class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r = len(board)
        c = len(board[0])

        o_in_border = set()
        o_checker = [[False]*c for _ in range(r)]

        def bfs(source):

            q = deque(source)

            while q:

                row, col = q.popleft()

                if o_checker[row][col]:
                    continue
                else:
                    o_checker[row][col] = True
                
                if 0<=row-1<r and board[row-1][col] == 'O':
                    q.append((row-1,col))
                if 0<=row+1<r and board[row+1][col] == 'O':
                    q.append((row+1,col))
                if 0<=col-1<c and board[row][col-1] == 'O':
                    q.append((row,col-1))
                if 0<=col+1<c and board[row][col+1] == 'O':
                    q.append((row,col+1))

        
        for i in range(r):
            if board[i][0] == 'O':
                o_in_border.add((i,0))
            if board[i][c-1] == 'O':
                o_in_border.add((i,c-1))
        
        for j in range(c):
            if board[0][j] == 'O':
                o_in_border.add((0,j))
            if board[r-1][j] == 'O':
                o_in_border.add((r-1,j))
        
        bfs(o_in_border)

        for x in range(r):
            for y in range(c):
                if not o_checker[x][y] and board[x][y] == 'O':
                    board[x][y] = 'X'
