class DSU:
    def __init__(self, n):
        # [0,1,2,3]
        # [0,0,0,2]
        self.parent = list(range(n))
        # [1,1,1,1]
        self.rank = [1] * n

    def find(self,k):
        cur = k

        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self,x,y) -> bool:
        u = self.find(x)
        v = self.find(y)

        if u == v:
            return False
        
        if self.rank[u] > self.rank[v]:
            u,v = v,u
        
        # v is bigger
        self.parent[u] = v
        self.rank[u] += self.rank[v]
        return True
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dsu
        dsu = DSU(n)
        res = n

        for a,b in edges:
            if dsu.union(a,b):
                res -= 1
        
        return res
