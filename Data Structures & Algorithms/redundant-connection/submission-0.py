class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        # do sth
        cur = x
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        
        return cur
    
    def union(self, i, j) -> List[int]:
        u = self.find(i)
        v = self.find(j)

        if u == v:
            # loop found
            return [i,j]
        
        if self.rank[u] > self.rank[v]:
            u, v = v, u
        
        # v is bigger
        self.parent[u] = v
        self.rank[u] += self.rank[v]
        return 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        res = []
    
        for a,b in edges:
            res = dsu.union(a,b)
            if res:
                return res