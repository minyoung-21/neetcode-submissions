class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]  
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            # x >= y
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if -x != -y:
                heapq.heappush(max_heap, -((-x)-(-y)))

        if max_heap:
            return -max_heap[0]
        else:
            return 0