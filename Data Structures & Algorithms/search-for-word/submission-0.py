class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(r:int,c:int,i:int) -> bool:
            if i == len(word):
                return True
                
            if r >= 0 and c >= 0 and r < len(board) and c < len(board[0]):
                if not check[r][c]:
                    if board[r][c] == word[i]:
                        check[r][c] = True
                        ans = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
                        check[r][c] = False
                        return ans
                    else:
                        return False
            
        for j in range(len(board)):
            for k in range(len(board[j])):
                if dfs(j,k,0):
                    return True

        return False