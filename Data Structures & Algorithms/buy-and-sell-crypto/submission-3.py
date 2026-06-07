class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0;

        for j in range(len(prices)):
            for i in range(j+1, len(prices)):
                if prices[j] < prices[i]:
                    res = max(res, prices[i] - prices[j])
            
        return res;