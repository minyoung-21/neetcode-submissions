class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            # not holding today: skip (result of not holding) vs buy (now + tmr profit)
            dp[i][0] = max(dp[i+1][0], -prices[i] + dp[i+1][1])
            # holding today: skip (result of holding) vs sell
            dp[i][1] = max(dp[i+1][1], prices[i] + dp[i+1][0])
        
        return dp[0][0]