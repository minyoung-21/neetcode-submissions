class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs

        ht = {i:[] for i in range(n)}
        visited = set()
        res = 0
        curr = 0

        for a,b in edges:
            ht[a].append(b)
            ht[b].append(a)

        def dfs(ch, pa, res) -> int:
            # do sth
            if ch in visited:
                return res
            
            visited.add(ch)
            
            for k in ht[ch]:
                if k == pa:
                    continue
                dfs(k, ch, res)

        for x in range(n):
            if x not in visited:
                res += 1
                dfs(x,-1,res)

        return res