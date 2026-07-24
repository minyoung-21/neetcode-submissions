class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        # making a table that maps neighbors
        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visit = set()
        t = 0
        
        while minHeap:
            # smallest
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            t = w1

            # traverse their neighbors
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    print(w1,w2, n2)
                    heapq.heappush(minHeap, (w1+w2, n2))
        
        return t if len(visit) == n else -1