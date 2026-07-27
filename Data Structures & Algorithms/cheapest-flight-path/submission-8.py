class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #bellman

        prices = [float("inf")]*n
        prices[src] = 0

        # allowed 2 stops means taking 3 flights
        for i in range(k+1):
            temp = prices.copy()

            for fr,to,pr in flights:
                if prices[fr] == float("inf"):
                    continue
                if prices[fr] + pr < temp[to]:
                    temp[to] = prices[fr] + pr
            prices = temp
        
        return prices[dst] if prices[dst] != float("inf") else -1