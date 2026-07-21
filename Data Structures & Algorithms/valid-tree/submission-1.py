class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ht = {i:[] for i in range(n)}
        visited = set()

        for a,b in edges:
            ht[a].append(b)
            ht[b].append(a)
        
        def dfs(child,parent) -> bool:
            # do sth
            if child in visited:
                return False
            visited.add(child)
            for k in ht[child]:
                if k == parent:
                    continue
                

                if not dfs(k,child):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n