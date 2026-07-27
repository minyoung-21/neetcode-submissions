class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #bellman

        prices = [float("inf")]*n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()

            for fr,to,price in flights:
                if prices[fr] == float("inf"):
                    continue
                if prices[fr] + price < temp[to]:
                    temp[to] = prices[fr] + price
            
            prices = temp
        
        return prices[dst] if prices[dst] != float("inf") else -1