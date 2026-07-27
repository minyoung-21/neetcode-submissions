class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u,v,t in times:
            edges[u].append((v,t))

        visit = set()
        q = [(0,k)]
        res = 0

        while q:
            dist,node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            res = dist

            for node2,weight in edges[node]:
                if node2 not in visit:
                    heapq.heappush(q,(weight+dist,node2))

        return res if len(visit) == n else -1