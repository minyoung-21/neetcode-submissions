class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sub = [], []
        l = len(s)

        def dfs(i:int):
            if i == l:
                res.append(sub.copy())
                return

            for j in range(i,l):
                piece = s[i:j+1]
                if piece == piece[::-1]:
                    sub.append(piece)
                    dfs(j+1)
                    sub.pop()
        
        dfs(0)
        return res