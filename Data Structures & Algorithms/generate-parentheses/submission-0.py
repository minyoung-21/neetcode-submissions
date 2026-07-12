class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o, c = 0, 0
        res, sub = [], []

        def dfs(o: int, c: int) -> str:
            if c > o or o > n:
                return 
            if len(sub) == 2*n:
                res.append("".join(sub))
                return
            sub.append('(')
            o += 1
            dfs(o,c)
            o -= 1
            sub.pop()
            sub.append(')')
            c += 1
            dfs(o,c)
            c -= 1
            sub.pop()
        
        dfs(0,0)
        return res