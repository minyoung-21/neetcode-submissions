class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ht = {i:[] for i in range(n)}
        visited = set()
        
        for f,s in edges:
            ht[f].append(s)
            ht[s].append(f)
        
        def dfs(node, parent) -> bool:
            # do sth

            if node in visited:
                return False
            
            visited.add(node)

            for k in ht[node]:
                if k == parent:
                    continue
                
                if not dfs(k, node):
                    return False

            # visited.remove(node)
            return True
        
        # for j in ht.keys():
        #     if not dfs(j):
        #         return False

        return dfs(0,-1) and len(visited) == n