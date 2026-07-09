class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # let's make it into a ht

        ht = {}

        for t in tasks:
            if t not in ht:
                ht[t] = 1
            else:
                ht[t] += 1

        # we need a way to count the interval

        heap = []

        for freq in ht.values():
            heap.append(-freq)
        
        heapq.heapify(heap)
        count = 0
        cool = deque()

        while heap or cool:
            count += 1

            while cool and cool[0][0] == count:
                available, freq = cool.popleft()
                heapq.heappush(heap, freq)

            if heap:
                to_pop = heapq.heappop(heap)
                if -to_pop > 1:
                    cool.append((count + n + 1, to_pop + 1))
            
            
        return count