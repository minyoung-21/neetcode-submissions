class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            min_heap.append([d, p[0], p[1]])
        
        heapq.heapify(min_heap)
        res = []

        for i in range(k):
            d, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        return res