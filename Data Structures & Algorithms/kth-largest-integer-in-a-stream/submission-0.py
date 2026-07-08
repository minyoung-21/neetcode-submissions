class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.i = k
        self.numl = nums

    def add(self, val: int) -> int:
        heapq.heapify(self.numl)
        heapq.heappush(self.numl, val)
        res = heapq.nlargest(self.i, self.numl)
        return res[-1]