class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sub = [], []
        l = len(digits)
        if l == 0:
            return res
        ht = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def dfs(i:int):
            if i == l:
                res.append("".join(sub))
                return
            
            for n in ht[digits[i]]:
                sub.append(n)
                dfs(i+1)
                sub.pop()
            
        dfs(0)
        return res