class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, sub = [], []

        def dfs(o: int, c: int):
            if o == c == n:
                res.append("".join(sub))
                return
            
            if o < n:
                sub.append('(')
                o += 1
                dfs(o,c)
                o -= 1
                sub.pop()
                
            
            if c < o:
                sub.append(')')
                c += 1
                dfs(o,c)
                c -= 1
                sub.pop()
                
        
        dfs(0,0)
        return res