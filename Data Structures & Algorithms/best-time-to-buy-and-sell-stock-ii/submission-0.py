class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        arr_len = len(prices)
        
        for i in range(1, arr_len):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]        
        return total