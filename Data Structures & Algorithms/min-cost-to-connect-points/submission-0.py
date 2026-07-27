class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = [False]*n
        node = 0
        dist = [10000000] * n
        res = 0
        edges = 0

        while edges < n-1:
            visit[node] = True
            nextNode = -1

            for i in range(n):
                if visit[i]:
                    continue
                
                new_dist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                
                dist[i] = min(dist[i], new_dist)

                if nextNode == -1 or dist[nextNode] > dist[i]:
                    nextNode = i
            
            edges += 1
            res += dist[nextNode]
            node = nextNode

        return res
