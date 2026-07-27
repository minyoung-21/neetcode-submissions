class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra's algo

        edges = collections.defaultdict(list)

        for f,t,p in flights:
            edges[f].append((t,p))
        
        visit = set()
        # cost, node, stops
        q = [(0,src,0)]
        best = {}

        while q:
            cost,node,stop = heapq.heappop(q)

            if node == dst:
                return cost
            
            if stop == k+1:
                continue
            
            if node in best and best[node] <= stop:
                continue
            
            best[node] = stop

            for des, price in edges[node]:
                heapq.heappush(q,(price+cost,des,stop+1))
        
        return -1